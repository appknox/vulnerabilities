
1. Wherever possible you must avoid storing sensitive data within your app.
2. Use libraries like SQLcipher to encrypt the information stored
3. set `"allow backup=false"` to avoid exploiting data using ADB

With the library SQLCipher, SQLite databases can be password-encrypted.

    SQLiteDatabase secureDB = SQLiteDatabase.openOrCreateDatabase(database, "password123", null);
    secureDB.execSQL("CREATE TABLE IF NOT EXISTS Accounts(Username VARCHAR,Password VARCHAR);");
    secureDB.execSQL("INSERT INTO Accounts VALUES('admin','AdminPassEnc');");
    secureDB.close();

If encrypted SQLite databases are used, determine whether the password is
hard-coded in the source, stored in shared preferences, or hidden somewhere
else in the code or filesystem. Secure ways to retrieve the key include:

- Asking the user to decrypt the database with a PIN or password once
  the app is opened (weak passwords and PINs are vulnerable to
  brute force attacks)
- Storing the key on the server and allowing it to be accessed from
  a web service only (so that the app can be used only when the device
  is online)
