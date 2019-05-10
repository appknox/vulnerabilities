
次のコードはjavax.net.ssl.SSLContextを継承しています。

    public void HostnameVerifier() {
        HostnameVerifier hv = new HostnameVerifier() {
            @Override
            public boolean verify(String hostname, SSLSession session) {
                // Always return true -> Accespt any host names
                return true;
            }
        };
    }

`HostnameVerifier`は、内容を確認したり、ホスト名を確認することなく常にtrueを返します。

