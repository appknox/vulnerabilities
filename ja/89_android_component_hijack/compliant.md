
Androidフレームワークは、信頼できないアプリケーションによって与えられたインテントのアクションを安全に実行するための "* PendingIntent *"メカニズムを提供します。場合によっては、この種の脆弱性に対する適切な対策となります。

    // Explicit intent to wrap
    Intent intent = new Intent(this, LoginActivity.class);

    // Create pending intent and wrap our intent
    PendingIntent pendingIntent = PendingIntent.getActivity(this, 1, intent, PendingIntent.FLAG_CANCEL_CURRENT);
    try {
        // Perform the operation associated with our pendingIntent
        pendingIntent.send();
    } catch (PendingIntent.CanceledException e) {
        e.printStackTrace();
    }

