
次の違反コードの例では、JavaScriptを有効にしてWebViewコンポーネントを使用し、検証なしでIntentを介して渡されたURIを処理します。

    public class MyBrowser extends Activity {
        @override
        public void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.main);

            WebView webView = (WebView) findViewById(R.id.webview);

            // turn on javascript
            WebSettings settings = webView.getSettings();
            settings.setJavaScriptEnabled(true);

            String turl = getIntent().getStringExtra("URL");
            webView.loadUrl(turl);
        }
    }

このコードは、この脆弱性がどのように悪用されるかを示しています。

    // Malicious application prepares some crafted HTML file,
    // places it on a local storage, makes accessible from
    // other applications. The following code sends an
    // intent to a target application (jp.vulnerable.android.app)
    // to make it access and process the malicious HTML file.

    String pkg = "jp.vulnerable.android.app";
    String cls = pkg + ".DummyLauncherActivity";
    String uri = "file:///[crafted HTML file]";
    Intent intent = new Intent();
    intent.setClassName(pkg, cls);
    intent.putExtra("url", uri);
    this.startActivity(intent);

