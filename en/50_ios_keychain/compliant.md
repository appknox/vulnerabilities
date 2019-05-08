
Store the sensitive data such as passwords in an encrypted form on the
device keychain so that even if the device is compromised no one can
infer correct passwords.

When storing data in the Keychain, use the most restrictive protection
class (as defined by `kSecAttrAccessible` attribute) that still allows
your application to function properly. For example, if your application
is not designed to be running in the background, use
`kSecAttrAccessibleWhenUnlocked` or `kSecAttrAccessibleWhenUnlockedThisDeviceOnly`

To prevent Keychain item exposure via iTunes backup, use one of
`...ThisDeviceOnly` protection classes if practical.

Finally, for highly sensitive data, consider augmenting protections
offered by the Keychain with application-level encryption. For example,
rely upon the user to enter a passphrase to authenticate within the
application and use that passphrase to encrypt data before storing it
into the Keychain.

    #define SALT_HASH @"FvTivqTqZXsgLLx1v3P8TGRyVHaSOB1pvfm02wvGadj7RLHV8GrfxaZ84oGA8RsKdNRpxdAojXYg9iAj"

    + (NSString *)securedSHA256DigestHashForPIN:(NSUInteger)pinHash
    {
        // 1
        NSString *name = [[NSUserDefaults standardUserDefaults] stringForKey:USERNAME];
        name = [name stringByAddingPercentEscapesUsingEncoding:NSUTF8StringEncoding];
        // 2
        NSString *computedHashString = [NSString stringWithFormat:@"%@%i%@", name, pinHash, SALT_HASH];
        // 3
        NSString *finalHash = [self computeSHA256DigestForString:computedHashString];
        NSLog(@" Computed hash: %@ for SHA256 Digest: %@", computedHashString, finalHash);
        return finalHash;
    }
    NSLog(@"User entered PIN");
    if ([textField.text length] > 0) {
        NSUInteger fieldHash = [textField.text hash];
        // 4
        NSString *fieldString = [KeychainWrapper securedSHA256DigestHashForPIN:fieldHash];
        NSLog(@" Password Hash - %@", fieldString);
        // Save PIN hash to the keychain (NEVER store the direct PIN)
        if ([KeychainWrapper createKeychainValue:fieldString forIdentifier:PIN_SAVED]) {
            [[NSUserDefaults standardUserDefaults] setBool:YES forKey:PIN_SAVED];
            [[NSUserDefaults standardUserDefaults] synchronize];
            NSLog(@" Key saved successfully to Keychain!!");
        }
    }

