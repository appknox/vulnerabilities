
TwitterクライアントアプリケーションであるMovatwiTouchは、コンテンツプロバイダーを使用して、Twitterのコンシューマー·キー、コンシューマー·シークレット、およびアクセストークンを管理していました。しかし、コンテンツプロバイダーが公開されると、ユーザのデバイスにインストールされたアプリケーションはこの機密情報にアクセスできるようになりました。
 AndroidManifest.xmlの次のエントリにはandroid：exported属性がありません。つまり、APIレベル16以前はコンテンツプロバイダが公開されていることを意味します。:
    <provider
        android:name=".content.AccountProvider"
        android:authorities="jp.co.vulnerable.accountprovider" />

