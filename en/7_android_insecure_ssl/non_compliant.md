
The following code implements a custom MySSLSocketFactory class that
inherits `javax.net.ssl.SSLContext`:

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

In the example above, the `InsecureSocketFactory` accepts all certificates
silently, which even bypasses the check for trustmanagers
