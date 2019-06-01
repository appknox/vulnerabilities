
アプリケーションは、重要な情報をログ出力に送信しないようにする必要があります。
アプリにサードパーティのライブラリが含まれている場合、開発者はライブラリが重要な情報をログとして出力しないようにする必要があります。
1つの一般的な解決策は、アプリケーションがカスタムログクラスを宣言して使用することです。そのため、ログ出力はDebug / Releaseに基づいて自動的にオン/オフされます。
開発者は ProGuard を使用して特定のメソッド呼び出しを削除できます。 これは、メソッドが副作用を含まないことを前提としています。

絶対にHTTP URLを使用してデータをダウンロードしないでください。代わりに、機密データのみをダウンロードできる有効なHTTPSリクエストを作成してください。
