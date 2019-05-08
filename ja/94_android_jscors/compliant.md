
以下は、Javascript CORS の問題を防ぐ方法の例です：

    WebSettings settings = getSettings();
    settings.setAllowUniversalAccessFromFileURLs(false)
    settings.setAllowFileAccessFromFileURLs(false)

