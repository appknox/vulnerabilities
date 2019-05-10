
これは、onReceivedSslErrorを使用してユーザとアプリケーションを停止または通知することで修正できます。

    public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error)  {
        //STOP OR ALERT THE USER
    }

