
This can be fixed by using the onReceivedSslError to stop or notify the
user and the application.

    public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error)  {
        //STOP OR ALERT THE USER
    }
