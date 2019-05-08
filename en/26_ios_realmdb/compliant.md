
It is suggested to use custom encryption while storing data in Realm
databases.

An encrypted copy of the unencrypted Realm file, which can be done by
using

    Realm().writeCopyToPath(_:encryptionKey:)

and then can use the encrypted file at the new location.
