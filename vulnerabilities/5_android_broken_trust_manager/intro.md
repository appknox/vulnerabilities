
Android apps that use SSL/TLS protocols for secure communication should
properly verify server certificates. The basic verification includes:

- verify that the subject (CN) of X.509 certificate and the URL
  matches
- verify that the certificate is signed by the trusted CA
- verify that the signature is correct
- verify that the certificate is not expired

A developer has the freedom to customize their SSL implementation. The
developer should properly use SSL as appropriate to the intent of the
app and the environment the apps are used in. If the SSL is not
correctly used, a user's sensitive data may leak via the vulnerable SSL
communication channel.

Fahl et al [Fahl
2012](https://wiki.sei.cmu.edu/confluence/display/java/Rule+AA.+References#RuleAA.References-Fahl2012)
describes the following patterns of the insecure use of SSL:

- Trusting All Certificates: The developer implements the
  TrustManager interface so that it will trust all the server
  certificate (regardless of who signed it, what is the CN etc.)
- Mixed-Mode/No SSL: A developer mixes secure and insecure
  connections in the same app or does not use SSL at all.

On Android, using `HttpURLConnection` is recommended for HTTP client
implementation.
