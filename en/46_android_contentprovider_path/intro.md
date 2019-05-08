
Content Providers are databases addressable by their application-defined
URIs. They are used for both persistent internal data storage and as a
mechanism for sharing information between applications.

By using the `ContentProvider.openFile()` method, you can provide a
facility for another application to access your application data (file).
Depending on the implementation of ContentProvider, use of the method
can lead to a directory traversal vulnerability. Hence, when exchanging
a file through a content provider, the path should be canonicalized
before it is used.
