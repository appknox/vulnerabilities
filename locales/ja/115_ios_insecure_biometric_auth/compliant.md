
以下は実装のサンプルです:

Keychain itemsにTouch ID保護を利用するには、`SecAccessControlCreateWithFlags()` API を使用して、security access control referenceを作成します。このAPIを使用する場合、user presence (`kSecAccessControlUserPresence`) ポリシーと、
`kSecAttrAccessibleWhenPasscodeSetThisDeviceOnly` の保護クラスを指定します。
その後、データを挿入するときに、返された `SecAccessControlRef` をattributes dictionary (key: `kSecAttrAccessControl`) で使用できます。

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
そして、keychainからデータを取得するために、以下を使用します:

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