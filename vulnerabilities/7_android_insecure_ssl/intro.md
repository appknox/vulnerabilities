
Android SDK 4.0 and later offers packages to implement capabilities to
establish network connections. For example, by using `java.net`
`javax.net` `android.net` `org.apache.http` a developer can create server
sockets or HTTP connection. `org.webkit` offers functions necessary to
implement web browsing capabilities.

A developer has the freedom to customize their SSL implementation. The
developer should properly use SSL as appropriate to the intent of the
app and the environment the apps are used in.

On Android, using `HttpURLConnection` is recommended for HTTP client
implementation.
