
Android版Facebook SDKには、Facebookのアクセストークンをプレーンテキスト形式のログ出力に送信する次のコードが含まれていました。

    Log.d("Facebook-authorize", "Login Success! access_token=" + getAccessToken() + " expires=" + getAccessExpires());

別の例として、 Android版 ウェザーニュースではユーザーの位置情報をログ出力に次のように送信していました。

    I/MyWeatherReport( 6483): Re-use MyWeatherReport data
    I/ ( 6483): GET JSON:
    http://example.com/smart/repo_piece.cgi?arc=0&lat=26.209026&lon=127.650803&rad=50&dir=-999&lim=52&category=1000

ユーザーが Android OS 4.0 以前を使用している場合、READ\_LOGS 権限を持つ他のアプリケーションは、マニフェストファイルで ACCESS\_FINE \_ LOCATION 権限を宣言せずにユーザーの場所情報を取得できます。

