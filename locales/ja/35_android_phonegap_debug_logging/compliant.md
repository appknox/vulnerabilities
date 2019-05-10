
Cordovaを使用している場合は、使用しているプラグインを公開してください。
    cordova build android --release

PhoneGapを使用している場合は、公開前にすべてのconsole.logs（）とその他のログコードをオフにしてください。

また、ログレベルは以下のように設定してください。
 "**INFO**" in "*config.xml*"

`<preference name="loglevel" value="INFO" />`
