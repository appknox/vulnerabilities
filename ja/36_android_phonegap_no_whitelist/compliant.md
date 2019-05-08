
Cordova が付随しているのは W3C Widget Access 仕様であり、それは特定のドメイン
へのネットワークアクセスを有効にする、アプリの config.xml file 内の <access>
要素に依存しています。 Command-Line インターフェースに記述されたCLI workflow 
に依存しているプロジェクトのため、このファイルはプロジェクトのトップレベル
ディレクトリに配置されています。他方でプラットフォーム固有の開発パスでは、場
所は次のセクションにリストされています：

次の例はホワイトリストの構文を例示しています：

google.com へのアクセス：

    <access origin="http://google.com" />

保護された google.com へのアクセス：

    <access origin="https://google.com" />

サブドメイン maps.google.com へのアクセス：

    <access origin="http://maps.google.com" />

google.com のすべてのサブドメイン（mail.google.com や docs.google.com など）へのアクセス：

    <access origin="http://*.google.com" />

すべてのドメイン（google.com、developer.mozilla.org など）へのアクセス：

    <access origin="*" />

これは、保護されていない新しく作成されたCLIプロジェクトのデフォルト値です。
