
In order to ensure that a Cordova WebView only allows requests to URLs
in the configured whitelist, the framework overrides Android's
`shouldInterceptRequest()`

The use of `shouldInterceptRequest()` to provide the whitelisting
mechanism is problematic in that it is used to intercept only certain
requests (such as those serviced over HTTP/S or through the file URI).
There may be protocols for which this function is not called by the
Android framework. As of Android 4.4 KitKat, the WebView is rendered by
Chromium and supports Web Sockets which one such protocol. An attacker
can therefore make use of a WebSocket connection to bypass the Cordova's
white-listing mechanism.
