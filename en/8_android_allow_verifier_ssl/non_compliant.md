
The following code extends `HttpClient` class that inherits
`javax.net.ssl.SSLContext`:

    public void allowAllHostnameVerifier() {
        SSLSocketFactory sf = null;

        sf.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
    }

This will enable the use of
`SSLSocketFactory.ALLOW\_ALL\_HOSTNAME\_VERIFIER` as a result, host
name verification that should take place when establishing an SSL
connection is disabled and will lead to the same situation as all the
certificate is trusted.
