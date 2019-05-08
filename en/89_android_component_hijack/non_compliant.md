
This application wants to create a user account in several trusted
applications using one broadcast intent:

    Intent intent = new Intent();
    intent.setAction("com.example.CreateUser");
    intent.putExtra("Username", uname_string);
    intent.putExtra("Password", pw_string);
    sendBroadcast(intent);

This application assumes only the trusted applications will be listening
for the action. A malicious application can register for this action and
intercept the user's login information, as below:

    IntentFilter filter = new IntentFilter("com.example.CreateUser");
    MyReceiver receiver = new MyReceiver();
    registerReceiver(receiver, filter);

When a broadcast contains sensitive information, create a whitelist of
applications that can receive the action using the application's manifest
file, or programmatically send the intent to each individual intended receiver.
