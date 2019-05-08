
Android apps that use SSL/TLS protocols for secure communication should
properly verify server certificates which should verify that the subject
(CN) of X.509 certificate and the URL matches

Allowing All Hostnames: The app does not verify if the certificate
issued is for the URL the client is connecting to. For example, when a
client connects to example.com, it will accept a server certificate
issued for some-other-domain.com.

On Android, using `HttpURLConnection` is recommended for HTTP client
implementation.
