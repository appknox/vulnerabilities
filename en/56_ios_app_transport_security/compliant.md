
App Transport Security (ATS) is enabled by default for apps linked
against the iOS 9.0 or later, as indicated by the default Boolean value
of NO for the NSAllowsArbitraryLoads key. This key is at the root level
of the NSAppTransportSecurity dictionary. With ATS enabled, HTTP
connections must use HTTPS. Attempts to connect using insecure HTTP
fail. ATS employs the Transport Layer Security (TLS) protocol version
1.2.

The `NSAppTransportSecurity` key is available in both apps and app
extensions. Starting in iOS 10.0 and later, the following subkeys are
supported:

- `NSAllowsArbitraryLoadsInMedia`
- `NSAllowsArbitraryLoadsInWebContent`
- `NSRequiresCertificateTransparency`
- `NSAllowsLocalNetworking`

For detailed documentation on configuring ATS, please read [Information Property List Key
Reference](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35).
