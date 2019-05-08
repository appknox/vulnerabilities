
The following code implements a custom `MySSLSocketFactory` class that
inherits `javax.net.ssl.SSLContext:`

    public void emptyTrustManager() throws IOException, KeyManagementException, NoSuchAlgorithmException {
        TrustManager tm = new X509TrustManager() {

            @Override
            public void checkClientTrusted(X509Certificate[] chain,
                    String authType) throws CertificateException {
                // Do nothing -> accept any certificates
            }

            @Override
            public void checkServerTrusted(X509Certificate[] chain,
                    String authType) throws CertificateException {
                // Do nothing -> accept any certificates
            }

            @Override
            public X509Certificate[] getAcceptedIssuers() {
                return null;
            }
        };
    }

In the example above, `checkClientTrusted()` and `checkServerTrusted()` are
overridden to make a blank implementation so that SSLSocketFactory does
not verify the SSL certificate. The MySSLSocketFactory class is used to
create an instance of HttpClient in another part of the application.
