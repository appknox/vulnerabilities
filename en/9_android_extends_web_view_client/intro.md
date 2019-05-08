
WebViews can introduce a number of security concerns and should be
implemented carefully. In particular, many vulnerabilities have been
discovered that exploit the use of the addJavscriptInterface API and
bypassing onReceivedSslError check.

WebView does support SSL/TLS, however, the blank screen is an indication
that the WebView does not believe that the certificate is valid. This
may happen with a certificate that is self-signed or a from a root auth
that is not set up in android. However if that check is bypassed, then
it removes all security from SSL.
