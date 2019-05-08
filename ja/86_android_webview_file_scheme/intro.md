
WebViewクラスは、Webページをアクティビティレイアウトの一部として表示します。
WebViewオブジェクトの動作は、WebView.getSettings（）から取得できるWebSettingsオブジェクトを使用してカスタマイズできます。

WebViewの主なセキュリティ上の懸念は、次のメソッドです。 `setJavaScriptEnabled（）`
 `setPluginState（）`
`setAllowFileAccess（）`

アクティビティにWebViewを埋め込んでWebページを表示すると、
どのようなアプリケーションでも、指定されたURIを持つインテントオブジェクトを作成してアクティビティに送信し、Webページの表示を要求することができます。

WebViewはさまざまなスキームを認識できますが、これには `file：scheme`も含まれます。
悪意のあるアプリケーションは、細工されたコンテンツを作成してローカルストレージ領域に保存し、MODE_WORLD_READABLE権限でアクセス可能にし、このコンテンツのURIを（target：file：schemeを使用して）ターゲットアクティビティに送信します。
