1) アプリケーションは、ユーザー名、ID、または安全ではない暗号化アルゴリズムに基づいて、容易に列挙できるアクセストークンを生成しています。

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: testuser
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: 560192
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: 5d9c68c6c50ed3d02a2fcf54f63993b6
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

2) アプリケーションは、バックエンドでセッショントークンを無効にしません。したがって、ユーザーがログアウトした後でも、有効期限が切れたトークンを使用して正常なリクエストを行い、ユーザーのリソースにアクセスすることが可能です。

3) 重要な機能の場合、リクエストが再送されたとき、アプリケーションは拒否する必要があります。例えば、チャージまたは支払いに関するリクエストが再送された場合、サーバは再送されたリクエストを拒否するべきです。

4) セッショントークンに有効期限がなく、無期限に有効な状態です。
