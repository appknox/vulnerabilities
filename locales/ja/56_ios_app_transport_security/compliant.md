
NSAlowsArbitraryLoads キーのデフォルトのブール値NOで示されるように、iOS 9.0以降にリンクされたアプリケーションの場合、App Transport Security（ATS）はデフォルトで有効になっています。このキーは、NSAppTransportSecurity  辞書のルートレベルにあります。ATSを有効にすると、HTTP接続でHTTPSを使用する必要があります。安全でないHTTPを使用して接続しようとすると失敗します。ATSはTransport Layer Security（TLS）プロトコルバージョン1.2を採用しています。

NSAppTransportSecurityキーは、アプリとアプリの両方の拡張機能で利用できます。次のサブキーがサポートされています。

- `NSAllowsArbitraryLoadsInMedia`
- `NSAllowsArbitraryLoadsInWebContent`
- `NSRequiresCertificateTransparency`
- `NSAllowsLocalNetworking`
ATSの設定に関する詳細なドキュメントについては
 [Information Property List Key Reference](https://developer.apple.com/library/content/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW35).を参照してください。
