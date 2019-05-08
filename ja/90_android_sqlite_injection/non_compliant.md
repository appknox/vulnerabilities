
SQLiteは、データを.dbファイルに保存するSQLデータベースエンジンです。Android SDKには、SQLiteデータベースのサポートが組み込まれています。
データベースの管理に使用される主なパッケージは、android.database.sqliteです。
機密情報をアクティビティ内に保存するには、次のコードを使用します。：

    SQLiteDatabase notSoSecure = openOrCreateDatabase("privateNotSoSecure",MODE_PRIVATE,null);
    notSoSecure.execSQL("CREATE TABLE IF NOT EXISTS Accounts(Username VARCHAR, Password VARCHAR);");
    notSoSecure.execSQL("INSERT INTO Accounts VALUES('admin','AdminPass');");
    notSoSecure.close();

アクティビティが呼び出されると、データベースファイル privateNotSoSecure が提供されたデータから作成され、平文ファイルが `/ data / data / <package-name> / databases / privateNotSoSecure`　に保存されます。
