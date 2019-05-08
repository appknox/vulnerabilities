
Android framework provides "*PendingIntent*" mechanism to safely perform the
actions of an intent given by untrusted apps. In some situations, it can be a
good measure for this kind of vulnerabilities.

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

