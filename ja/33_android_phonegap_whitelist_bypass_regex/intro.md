
Cordova WebView が設定されたホワイトリストのURLへのリクエストのみを許可するために、フレームワーク は Android の shouldInterceptRequest（）をオーバーライドします。

ホワイトリスト作成メカニズムを提供するために shouldInterceptRequest（）を使用することは、特定の要求（HTTP / HTTPSを介して処理されるものやファイルURIを介して処理されるものなど）のみを傍受するために使用される点で問題があります。
Android フレームワークがこの関数を呼び出せないプロトコルがあります。 Android 4.4 KitKatでは、WebView は Chromium によってレンダリングされ、そのようなプロトコルの1つである Web Sockets をサポートしています。 したがって、攻撃者は WebSocket 接続を利用して、Cordova のホワイトリストメカニズムをバイパスすることができます。
