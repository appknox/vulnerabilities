
たとえデバイスが侵害されても、誰も正しいパスワードを察知できないように、パスワードのような重要データは暗号化されたフォームでデバイスキーチェーン上に保存してください。
データをキーチェーンに保存するときは、あなたのアプリが正常に機能することを許可する、最も厳しい保護クラスを使用してください（kSecAttrAccessible attribute によって定義されたように）。例えば、もしあなたのアプリがバックグラウンドで実行するよう設計されていないなら、 kSecAttrAccessibleWhenUnlocked または kSecAttrAccessibleWhenUnlockedThisDeviceOnly を使用してください。
キーチェーンアイテムの iTunes バックアップ経由での露出を防ぐために、もし実用的なら...ThisDeviceOnly 保護クラスの一つを使用してください。
最後に、高度に重要なデータのためにキーチェーンによって提供されるアプリレベルの暗号化での保護の増量を考えてください。例えば、ユーザーをアプリ内での認証のためのパスフレーズに入るようにし、キーチェーンにそれを保存する前にパスフレーズを使いデータを暗号化してください。

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

