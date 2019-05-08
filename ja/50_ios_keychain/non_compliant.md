
OWASP Mobile Top 10 の M8 に非準拠  - Side Channel Data Leakage
ピンコードがセキュリティで保護されずに保存されるキーチェーンの実装例：
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

