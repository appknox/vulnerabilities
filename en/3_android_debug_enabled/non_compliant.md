
This non-compliant code example shows an app that has the
`android:debuggable` attribute set to true being accessed to reveal
sensitive data.

    $ adb shell
    shell@android:/ $ run-as com.example.someapp sh
    shell@android:/data/data/com.example.someapp $ id
    uid=10060(app_60) gid=10060(app_60)
    shell@android:/data/data/com.example.someapp $ ls files/
    secret_data.txt
    shell@android:/data/data/com.example.some $ cat files/secret_data.txt
    password=GoogolPlex
    account_number=31974286

Clearly, with the `android:debuggable` attribute set to true, sensitive
date related to the app can be revealed to any user.
