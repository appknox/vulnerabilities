
この規格に準拠していないコード例は、android:debuggable 属性が true に設定されていて機密データを漏らすためにアクセスされるアプリケーションを示しています。

    $ adb shell
    shell@android:/ $ run-as com.example.someapp sh
    shell@android:/data/data/com.example.someapp $ id
    uid=10060(app_60) gid=10060(app_60)
    shell@android:/data/data/com.example.someapp $ ls files/
    secret_data.txt
    shell@android:/data/data/com.example.some $ cat files/secret_data.txt
    password=GoogolPlex
    account_number=31974286

`android：debuggable`属性が true に設定されていると、アプリに関連する機密性の高いデータが漏洩することがあります。
