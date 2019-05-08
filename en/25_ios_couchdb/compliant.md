
It is suggested to use custom encryption while storing data in Couch
Database.

Database encryption is available for both ForestDB and SQLite storage
types. It is automatically hooked into ForestDB's filesystem abstraction
layer and for SQLite storage, Couchbase Lite uses SQLCipher; an open
source extension to SQLite that provides transparent encryption of
database files. In both cases, the encryption specification is 256-bit
AES.

SQLCipher is an optional dependency. The section below describes how to
add it to platform.

- Download the iOS SDK from [here](http://www.couchbase.com/nosql-databases/downloads#couchbase-mobile).
- Add the libsqlcipher.a library to your XCode project.
- Go to the Link Binary With Libraries build phase of your app target.
- Remove libsqlite.dylib

