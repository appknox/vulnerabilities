
トラストバウンダリ外からインテント経由で受信したURIは、WebViewでレンダリングする前に検証する必要があります。たとえば、次のコードは受信したURIをチェックし、それが `file：scheme` URIでない場合にのみ使用します。

    String intentUrl = getIntent().getStringExtra("url");
    String localUrl = "about:blank";
    if (!intentUrl.startsWith("file:")) {
        loadUrl = intentUrl;
    }

