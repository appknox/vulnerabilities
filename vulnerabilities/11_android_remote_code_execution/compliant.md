
-   Compliant code could refrain from calling the addJavascriptInterface() method.

        WebView webView = new WebView(this);
        setContentView(webView);

-   Another compliant solution is to specify in the app's manifest that
    the app is only for API levels JELLY\_BEAN\_MR1 and above. For these
    API levels, only public methods that are annotated with
    JavascriptInterface can be accessed from JavaScript. API level 17
    is JELLY\_BEAN\_MR1.

        <manifest>
            <uses-sdk android:minSdkVersion="17" />
            ...
        </manifest>

