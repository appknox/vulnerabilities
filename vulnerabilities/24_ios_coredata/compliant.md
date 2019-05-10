
It is suggested to use custom encryption while storing data in Core
Data.

EncryptedStore is known to work successfully on iOS versions 6.0 through
9.3.4 to store CoreData in encrypted format

If you wish to set a custom cache size and/or custom database URL:
create an NSDictionary to set the options for your EncryptedStore,
replacing customPasscode, customCacheSize, and/or customDatabaseURL:

    NSDictionary *options = @{ EncryptedStorePassphraseKey: (NSString *) customPasscode,
                               EncryptedStoreCacheSize: (NSNumber *) customCacheSize,
                               EncryptedStoreDatabaseLocation: (NSURL *) customDatabaseURL
    };

In your application delegate source file (i.e. AppDelegate.m) you should see

    NSPersistentStoreCoordinator *coordinator = [self persistentStoreCoordinator];

If you created an NSDictionary with custom options, replace that line with

    NSPersistentStoreCoordinator *coordinator = [EncryptedStore makeStoreWithOptions:options managedObjectModel:[self managedObjectModel]];

The project is available [here](https://github.com/project-imas/encrypted-core-data).
