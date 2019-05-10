
このアプリケーションは、ひとつのブロードキャストインテントを使用して、複数の信頼できるアプリケーションでユーザーアカウントを作成する必要があります。

    Intent intent = new Intent();
    intent.setAction("com.example.CreateUser");
    intent.putExtra("Username", uname_string);
    intent.putExtra("Password", pw_string);
    sendBroadcast(intent);

このアプリケーションは、信頼できるアプリケーションだけがアクションをリッスンすることを想定しています。悪意のあるアプリケーションはこのアクションに登録し、以下のようにユーザのログイン情報を傍受することができます：
    IntentFilter filter = new IntentFilter("com.example.CreateUser");
    MyReceiver receiver = new MyReceiver();
    registerReceiver(receiver, filter);

ブロードキャストに機密情報が含まれている場合は、アプリケーションのマニフェストファイルを使用してアクションを受け取ることができます。アプリケーションのホワイトリストを作成するか、個々のレシーバーにインテントをプログラムで送信します。
