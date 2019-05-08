
Androidの多くの電子メールアプリとメッセージングアプリは、Androidのギャラリーなどの他のアプリから共有されたファイルを送信するためにIntent APIを利用しています。
これらのインテントは、コンテンツの送受信に標準化されています。
このAPIを介して動画などのファイル全体を送信する代わりに、実際の保存場所を指すURIだけが交換されます。このIntent APIの脆弱性は、特権の昇格やデータ漏洩を可能にする、公開された多くの通信アプリに存在します。

主な問題は、アプリが自分のプライベートデータにアクセスできるだけでなく
`Context.openFileOutput（文字列名、intモード）`を使用するディレクトリ、
_file_ URIも使用します。
これらのURIは通常、SDカード上のファイルにアクセスするために使用されますが、例えば、file：/// sdcard / paper.pdf を介して、file：/// data / data / com.example.app / files / paper.pdf のようなプライベートファイルを指定することもできます。アプリがインテントフィルタを登録してAndroidの共有APIをサポートするか、URIを受け取るカスタムインテントを定義する場合、潜在的に自分自身のプライベートファイルを指す可能性のある_file_ URIを許容します。
電子メールやメッセージングアプリのようなコミュニケーションを容易にするアプリでは、これを「Surreptitious Sharing」と呼びます。
AOSPのソースコードを調べると、 `OpenOsetFileDescriptor`の中にContext.openFileOutput（String name、int mode） `を使った_file_ URIのサポートが削除される予定だったことが明らかになりました。（次の` openInputStream`メソッドのインラインコメントを参照してください。
[ContentResolver]
(https://goo.gl/Qyx84j)).
