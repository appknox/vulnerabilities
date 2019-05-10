
AndroidManifest.xmlファイルの次のエントリは、他のアプリがデータにアクセスできないようにコンテンツプロバイダを非公開にします。

    <provider
        android:name=".content.AccountProvider"
        android:exported="false"
        android:authorities="jp.co.vulnerable.accountprovider" />

