
この攻撃は、TLSの再ネゴシエーション機能を悪用したもので、すでにTLS接続を行っているクライアントとサーバーが、新しいパラメータのネゴシエーションや新しい鍵の生成などを行うことができるものです。再交渉は既存のTLS接続内で行われ、新しいハンドシェイクパケットはアプリケーションパケットと一緒に暗号化されます。他のチャンネルに結びつかず、攻撃者にウィンドウを与えてしまうことが難点です。
