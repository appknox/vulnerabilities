
Example of an insecure code:

    db.rawQuery("SELECT username FROM users_table WHERE id = '"+ input_id +"'");
    db.execSQL("SELECT username FROM users_table WHERE id = '"+ input_id +"'");

