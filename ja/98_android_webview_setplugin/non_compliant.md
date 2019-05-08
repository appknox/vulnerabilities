
以下は、安全でない実装の例です。
    WebSettings settings = webView.getSettings();
    settings.setPluginsEnabled(true);
    settings.setPluginState(WebSettings.PluginState.ON);

