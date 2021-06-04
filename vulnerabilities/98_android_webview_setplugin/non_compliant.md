
Following is an example of insecure implementation

    WebSettings settings = webView.getSettings();
    settings.setPluginsEnabled(true);
    settings.setPluginState(WebSettings.PluginState.ON);

