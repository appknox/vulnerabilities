
This non-compliant code example shows an application that calls the
`addJavascriptInterface()` method, and hence is not secure for API level
JELLY\_BEAN and lower.

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

JavaScript can now control the host. Java reflection could be used to
access any of the public methods of an injected object, using the
permissions of the app.
