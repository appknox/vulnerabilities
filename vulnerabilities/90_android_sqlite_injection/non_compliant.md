
SQLite is an SQL database engine that stores data in .db files.
The Android SDK has built-in support for SQLite databases.
The main package used to manage the databases is android.database.sqlite.
You may use the following code to store sensitive information within an
activity:

    SQLiteDatabase notSoSecure = openOrCreateDatabase("privateNotSoSecure",MODE_PRIVATE,null);
    notSoSecure.execSQL("CREATE TABLE IF NOT EXISTS Accounts(Username VARCHAR, Password VARCHAR);");
    notSoSecure.execSQL("INSERT INTO Accounts VALUES('admin','AdminPass');");
    notSoSecure.close();

Once the activity has been called, the database file privateNotSoSecure will
be created with the provided data and stored in the clear text
file `/data/data/<package-name>/databases/privateNotSoSecure`
