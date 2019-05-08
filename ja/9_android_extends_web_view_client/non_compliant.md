
次のコードは、onReceivedSslError を使用して WebViewClient のチェックをバイパスする方法を示しています。

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

