
CoreDataにデータ保存する際、カスタム暗号化の使用が推奨されます。
EncryptedStoreはCoreDataを暗号化形式で保存するためにiOSバージョン6.0～9.3.4で正常に動作することが知られています。
もしカスタムキャッシュサイズ、あるいはカスタムデータベースURLをセットしたいなら、カスタムパスコード、カスタムキャッシュサイズ、および/またはカスタムデータベースURLの代わりに、あなたのEncryptedStoreのオプションをセットするNSDictionaryを作成してください。

    NSDictionary *options = @{ EncryptedStorePassphraseKey: (NSString *) customPasscode,
                               EncryptedStoreCacheSize: (NSNumber *) customCacheSize,
                               EncryptedStoreDatabaseLocation: (NSURL *) customDatabaseURL
    };

In your application delegate source file (i.e. AppDelegate.m) you should see

    NSPersistentStoreCoordinator *coordinator = [self persistentStoreCoordinator];

If you created an NSDictionary with custom options, replace that line with

    NSPersistentStoreCoordinator *coordinator = [EncryptedStore makeStoreWithOptions:options managedObjectModel:[self managedObjectModel]];

The project is available [here](https://github.com/project-imas/encrypted-core-data).
