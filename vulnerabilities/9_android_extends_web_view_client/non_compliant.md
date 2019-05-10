
The following code shows how onReceivedSslError was used to bypass the
check in WebViewClient:

    public class SSLAcceptingWebViewClient extends CordovaWebViewClient {
        public SSLAcceptingWebViewClient(DroidGap ctx) {
            super(ctx);
        }
        @Override
        public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {
            //proceed or pass
            handler.proceed(); // Ignore SSL certificate errors
        }

    }

