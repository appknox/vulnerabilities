
- 準拠しているコードでは、addJavascriptInterface()メソッドの呼び出しを控えることができます。

        WebView webView = new WebView(this);
        setContentView(webView);

- もう1つの準拠した解決策は、アプリケーションがAPIレベルJELLY_BEAN_MR1以上のみ用であることをアプリケーションのマニフェストに指定することです。これらのAPIレベルに対しては、JavascriptInterfaceでアノテーションされたパブリックメソッドのみがJavaScriptからアクセスできます。APIレベル17はJELLY_BEAN_MR1です。     

        <manifest>
            <uses-sdk android:minSdkVersion="17" />
            ...
        </manifest>

