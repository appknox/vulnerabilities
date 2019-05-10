
Allowing All Hostnames: The app does not verify if the certificate is
issued for the URL the client is connecting to. For example, when a
client connects to example.com, it will accept a server certificate
issued for some-other-domain.com.

On Android, using `HttpURLConnection` is recommended for HTTP client
implementation.
