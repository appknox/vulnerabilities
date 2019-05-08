
Not in compliance with OWASP Mobile Top 10 for M8 - Side Channel Data
Leakage Example keychain implementation where the pincode is stored
insecurely:

    NSLog(@"User entered PIN");
    if ([textField.text length] > 0) {
        NSUInteger fieldHash = [textField.text hash];

        NSLog(@" Password Is - %@", fieldString);

        // Save PIN  to the keychain (NEVER store the direct PIN)
        if ([KeychainWrapper createKeychainValue:fieldString forIdentifier:PIN_SAVED]) {
            [[NSUserDefaults standardUserDefaults] setBool:YES forKey:PIN_SAVED];
            [[NSUserDefaults standardUserDefaults] synchronize];
            NSLog(@" Key saved successfully to Keychain!!");
        }
    }

