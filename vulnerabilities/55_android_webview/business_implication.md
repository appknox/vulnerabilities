
An improperly implemented WebView instance may be vulnerable to XSS can
be used to gain access to shared preference files using `file:///`. When
Javascript is enabled, it may allow adversaries to perform XSS attacks.
Furthermore, not loading WebView over HTTPS may allow attackers to sniff
data from network transmissions and perform Man-in-the-Middle attack by
injecting arbitrary JavaScript into the WebView.
