
RealmDBにデータ保存する際、カスタム暗号化の使用が推奨されます。
暗号化されていないRealmファイルの暗号化コピー 

    Realm().writeCopyToPath(_:encryptionKey:)

新しいロケーションで暗号化されたファイルを使用することができます。
