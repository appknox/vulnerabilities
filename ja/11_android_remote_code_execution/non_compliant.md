
この非準拠のコード例は、 `addJavascriptInterface（）`メソッドを呼び出すアプリケーションを示しているため、APIレベル JELLY \ _ BEAN 以下では安全ではありません。

    WebView webView = new WebView(this);
    setContentView(webView);...
    class JsObject {
        private String sensitiveInformation;
        ...
        public String toString() {
            return sensitiveInformation;
        }
    }
    webView.addJavascriptInterface(new JsObject(), "injectedObject");
    webView.loadData("", "text/html", null);
    webView.loadUrl("http://www.example.com");

JavaScript がホストを制御できるようになりました。 Javaリフレクションは、アプリケーションのパーミッションを使用して、注入されたオブジェクトの public メソッドにアクセスするために使用できます。
