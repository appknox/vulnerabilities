
以下のコードは `javax.net.ssl.SSLContext：`を継承するカスタム`MySSLSocketFactory`クラスを実装しています。

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

上記の例では、 `checkClientTrusted（）`と `checkServerTrusted（）`は、SSLSocketFactoryがSSL証明書を検証しないように空の実装を作るためにオーバーライドされています。MySSLSocketFactoryクラスは、アプリケーションの別の部分にHttpClientのインスタンスを作成するために使用されます。
