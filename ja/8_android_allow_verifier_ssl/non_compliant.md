
次のコードは、javax.net.ssl.SSLContextを継承するHttpClientクラスを拡張しています。：

    public void allowAllHostnameVerifier() {
        SSLSocketFactory sf = null;

        sf.setHostnameVerifier(SSLSocketFactory.ALLOW_ALL_HOSTNAME_VERIFIER);
    }

これにより、結果として `SSLSocketFactory.ALLOW \ _ ALL \ _ HOSTNAME \ _ VERIFIER`を使用できるようになります。
SSL接続の確立時に行われるホスト名の検証は無効になり、すべての証明書が信頼されるのと同じ状況になります。

