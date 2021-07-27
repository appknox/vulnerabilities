
Here is a sample implementation:

To utilise Touch ID protection for Keychain items, create a security access control
reference using the `SecAccessControlCreateWithFlags()` API. When using this API,
specify the user presence (`kSecAccessControlUserPresence`) policy and a protection
class of `kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly`. You can then use the
returned `SecAccessControlRef` in the attributes dictionary (key:
`kSecAttrAccessControl`) when inserting the data.

    #define HEX_SERVICE @"HEX_EXAMPLE_SERVICE"
    #define HEX_SERVICE_MSG @"Authenticate to unlock the key"

        SecAccessControlRef sacRef;
        CFErrorRef *err = nil;

        /*
        Important considerations.
        Please read the docs regarding kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly.
        TL;DR - If the user unsets their device passcode, these keychain items are destroyed.
        You will need to add code to compensate for this, i.e to say that touch ID can only be used if the device has a passcode set.

        Additionally, keychain entries with this flag will not be backed up/restored via iCloud.
        */

        //Gets our Security Access Control ref for user presence policy (requires user AuthN)
        sacRef = SecAccessControlCreateWithFlags(kCFAllocatorDefault,
                    kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly,
                    kSecAccessControlBiometryAny,
                    kSecAccessControlUserPresence,
                    err);

        NSDictionary *attributes = @{
            //Sec class, in this case just a password
            (__bridge id)kSecClass: (__bridge id)kSecClassGenericPassword,
            //Our service UUID/Name
            (__bridge id)kSecAttrService: HEX_SERVICE,
            //The data to insert
            (__bridge id)kSecValueData: [@"sup3r_s3cur3_k3y"
                                            dataUsingEncoding:NSUTF8StringEncoding],
            //Whether or not we want to prompt on insert
            (__bridge id)kSecUseNoAuthenticationUI: @YES,
            //Our security access control reference
            (__bridge id)kSecAttrAccessControl: (__bridge_transfer id)sacRef
        };

        dispatch_async(dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
            //Insert the data to the keychain, using our attributes dictionary
            OSStatus status = SecItemAdd((__bridge CFDictionaryRef)attributes, nil);
        });

    }
And now to obtain the data from the keychain, use the following:

    /* Lets get our secret from the keychain.
    * User will be asked for Touch ID or device passcode if Touch ID not available
    * You could use LocalAuthentication's canEvaluatePolicy method to determine if this is a touch ID device first.
    */
    NSDictionary *query = @{
        (__bridge id)kSecClass: (__bridge id)kSecClassGenericPassword,
        (__bridge id)kSecAttrService: HEX_SERVICE,
        (__bridge id)kSecReturnData: @YES,
        (__bridge id)kSecUseOperationPrompt: HEX_SERVICE_MSG
    };

    dispatch_async(dispatch_get_global_queue( DISPATCH_QUEUE_PRIORITY_DEFAULT, 0), ^{
        CFTypeRef dataTypeRef = NULL;

        OSStatus status = SecItemCopyMatching((__bridge CFDictionaryRef)(query), &dataTypeRef);
        if (status == errSecSuccess)
        {
            NSData *resultData = ( __bridge_transfer NSData *)dataTypeRef;

            NSString * result = [[NSString alloc]
                                    initWithData:resultData
                                    encoding:NSUTF8StringEncoding];

            //Show alertview on main queue
            dispatch_async(dispatch_get_main_queue(), ^{
                NSLog(@"Keychain entry: %@", result);
                UIAlertView *alert = [[UIAlertView alloc]
                                        initWithTitle: @"Thanks"
                                        message:[NSString stringWithFormat:
                                                    @"The key is: %@", result]
                                        delegate:self
                                        cancelButtonTitle:@"OK"
                                        otherButtonTitles:nil];
                [alert show];
            });
        }
        else
        {
            //Normally would do better error handling
            NSLog(@"Something went wrong");
        }
    });
