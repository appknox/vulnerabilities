
CouchDBにデータ保存する際、カスタム暗号化の使用が推奨されます。</p> <p> データベース暗号化はForestDBとSQLiteストレージタイプの両方で利用できます。それは自動的にForestDBのファイルシステムの抽象化レイヤーにフックされ、SQLiteストレージにはCouchbase LiteがSQLCipherを使用します。それはデータベースファイルの透過的な暗号化を付与するSQLiteのオープンソース拡張機能です。両方の場合において、暗号化仕様は256-bit AESです。</p> <p> SQLCipherは任意の依存関係です。次のセクションはそれをプラットフォームに追加する方法を記述しています。

- 次のURLからiOS SDKをダウンロード: <a href="http://www.couchbase.com/nosql-databases/downloads#couchbase-mobile">http://www.couchbase.com/nosql-databases/downloads#couchbase-mobile</a>.
- Xcodeプロジェクトにlibsqlcipher.aライブラリを追加してください。</li>     <li>あなたのapp targetのLink Binary With Librariesビルドフェーズに進んでください。
- libsqlite.dylibを除去してください。

