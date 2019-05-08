
1.可能な限り、機密データをアプリに保存しないようにする必要があります。
2. SQLCipherのようなライブラリを使用して、格納されている情報を暗号化します。
3.「allow backup = false」を設定してADBを使用したデータの悪用を回避します。

ライブラリSQLCipherでは、SQLiteデータベースをパスワードで暗号化できます。

    SQLiteDatabase secureDB = SQLiteDatabase.openOrCreateDatabase(database, "password123", null);
    secureDB.execSQL("CREATE TABLE IF NOT EXISTS Accounts(Username VARCHAR,Password VARCHAR);");
    secureDB.execSQL("INSERT INTO Accounts VALUES('admin','AdminPassEnc');");
    secureDB.close();

暗号化されたSQLiteデータベースが使用されている場合は、パスワードがソースでハードコーディングされているか、共有設定に保存されているか、またはコードやファイルシステムのどこかに隠れているかどうかを判断します。キーを取得する安全な方法には、次のようなものがあります。

 - アプリケーションが開かれた後、PINまたはパスワードを使用してデータベースを復号するようにユーザーに尋ねる（弱いパスワードとPINはブルートフォース攻撃に対して脆弱です。）
- サーバーにキーを格納し、Webサービスからのみアクセスできるようにする（デバイスがオンラインのときだけアプリケーションを使用できるようにする）
