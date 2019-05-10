
Any URI received via an intent from outside a trust-boundary should be
validated before rendering it with WebView. For example,
the following code checks an received URI and uses it only when it
is not a `file:scheme` URI.

    String intentUrl = getIntent().getStringExtra("url");
    String localUrl = "about:blank";
    if (!intentUrl.startsWith("file:")) {
        loadUrl = intentUrl;
    }

