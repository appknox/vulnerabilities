
次のコードは、 `javax.net.ssl.SSLContext`を継承するカスタムのMySSLSocketFactory クラスを実装しています。：


    public class InsecureSocketFactory extends SSLSocketFactory {
        protected SSLSocketFactory _factory;
        public InsecureSocketFactory() {
            try {
                SSLContext ctx = SSLContext.getInstance("SSL");
                ctx.init(null, new TrustManager[] { new InsecureTrustManager() }, null);
                _factory = ctx.getSocketFactory();
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }

上記の例では、 `InsecureSocketFactory`はすべての証明書を黙って受け取り、trustmanager のチェックをバイパスします。
