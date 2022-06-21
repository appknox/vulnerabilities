
ウェブサーバーのTRACEメソッドを無効にしてください。

使用するサーバーの種類によって、以下のような設定が可能です:

Apache
======
これらのメソッドを無効にするには、各virtual hostの設定ファイルに以下の行を追加してください :

    RewriteEngine on
    RewriteCond %{REQUEST_METHOD} ^(TRACE|TRACK)
    RewriteRule .* – [F]

あるいは、Apacheのバージョン 1.3.34, 2.0.55, 2.2 は ‘TraceEnable’ ディレクティブを介してTRACE メソッドをネイティブに無効にすることをサポートしていることに留意してください。

Microsoft IIS
==============
TRACKメソッドは、MicrosoftのURLScan DenyVerbs セクションに追加することができます。urlscan.ini fileのAllowVerbs セクションにするべきではありません。

URLスキャンツールを使用して、HTTP TRACEリクエストを拒否したり、サイトの要件やポリシーを満たすために必要なメソッドのみを許可することができます。Urlscan 2.5（baselineとSRP）のデフォルト設定は、GETとHEADのメソッドのみを許可します。

NGINX
======
ほとんどの Web サイトは、GET、HEAD、POST、 HTTP のメソッドのみを必要とします。TRACEまたはDELETEメソッドを有効にすると、サーバーがクロスサイトトラッキング攻撃にさらされる危険性があります。

クロスサイトトレーシング攻撃を軽減するために、default.confファイルを修正し「server block」の下に以下を追加します。 

    if ($request_method !~ ^(GET|HEAD|POST)$ )
    {
        return 405;
    }

DELETE、TRACE、PUT、OPTIONSメソッドを使用しようとすると、「405 - Not Allowed」が返されるよう修正します。
