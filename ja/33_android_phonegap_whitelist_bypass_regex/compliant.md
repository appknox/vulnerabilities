
ドメインホワイトリストは、アプリケーションが制御できない外部ドメインへのアクセスを制御するセキュリティモデルです。 Cordovaのデフォルトのセキュリティポリシーでは、どのサイトにもアクセスできます。 アプリケーションを本番環境に移行する前に、ホワイトリストを作成し、特定のネットワークドメインとサブドメインにアクセスできるようにする必要があります。
Cordovaは、特定のドメインへのネットワークアクセスを可能にするために、アプリケーションの `config.xml`ファイル内の `<access>` 要素に依存するW3C Widget Access仕様に準拠しています。 コマンドラインインターフェイスで説明されているCLIワークフローに依存するプロジェクトの場合、このファイルはプロジェクトの最上位ディレクトリにあります。 それ以外のプラットフォーム固有の開発パスの場合は、次のセクションで場所を示します。：
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

また、PhoneGapまたはApache Cordovaアプリケーションを最新バージョンにアップグレードしてください。
