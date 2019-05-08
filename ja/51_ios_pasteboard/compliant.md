
<p>特定のペーストボードアプリを使用してください。また、データが絶対にコピーされないよう保護されたパスワードのようなフィールドをマークしてください。 </p> <p>ペーストボードはパブリックあるいはプライベートになり得ます。 パブリックペーストボードはシステムペーストボードと呼ばれます。 プライベートペーストボードはアプリによって作成され、そのためアプリペーストボードと呼ばれます。ペーストボードはユニークな名前を持つ必要があります。

- `UIPasteboardNameGeneral`は、広範囲のデータ型を含むカット、コピー、ペーストの操作用です。汎用ペーストボードを表すシングルトンオブジェクトを取得するには、generalPasteboardクラスメソッドを呼び出します。

- `UIPasteboardNameFind`は検索操作のためのものです。
検索バーのユーザーが現在入力した文字列（ `UISearchBar`）はこのペーストボードに書き込まれ、アプリ間で共有できます。 FindPasteboardを表すオブジェクトを取得するには、pasteboardWithName：create：classメソッドを呼び出し、UIPasteboardNameFindで名前を渡します。

通常、システム定義のペーストボードの1つを使用しますが、必要に応じてpasteboardWithNameを使用して独自のアプリペーストボードを作成できます。create：pasteboardWithUniqueNameを呼び出すと、UIPasteboardは固有の名前のアプリペーストボードを提供します。ペーストボードの名前は、そのnameプロパティで検出できます。

アプリケーションがバックグラウンドになると、ペーストボードをクリアします。
これを行うには、メソッドに次の行を追加します。
`- (void)applicationDidEnterBackground:(UIApplication \*)` application in AppDelegate.

If you are using a custom Pasteboard, replace `[UIPasteboard generalPasteboard]` with your custom pasteboard.

    - (void)applicationDidEnterBackground:(UIApplication *)application
    {
        // Use this method to release shared resources, save user data, invalidate
        timers, and store enough application state information to restore your application
        to its current state in case it is terminated later.

        // If your application supports background execution, this method is called
        instead of applicationWillTerminate: when the user quits.

        [UIPasteboard generalPasteboard].items = nil;
    }

