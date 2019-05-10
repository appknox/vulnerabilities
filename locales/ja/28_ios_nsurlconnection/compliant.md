
Appleが近い将来 NSURLConnection のサポートを停止する可能性があるため、すべてのタイプのネットワーク接続に、NSURLConnection の代わりとして NSURLSession を使用することをお勧めします。

NSURLSessionは、HTTPリクエストの送受信を担うキーオブジェクトです。 NSURLSessionConfiguration を介して作成することができます。これには3つの種類があります。

`defaultSessionConfiguration`：ストレージに永続化されたキャッシュ、資格情報およびcookieのストレージを使用するデフォルト設定オブジェクトを作成します。

`ephemeralSessionConfiguration`：defaultSessionConfiguration と似ていますが、すべてのセッション関連のデータがメモリに格納される点が異なります。これを「プライベートセッション」と考えてください。

`backgroundSessionConfiguration`：セッションがバックグラウンドでアップロードまたはダウンロードタスクを実行できるようにします。アプリケーション自体が一時停止または終了してもセッションは継続されます。

NSURLSessionConfigurationでは、タイムアウト値、キャッシュポリシー、追加のHTTPヘッダーなどのセッションプロパティーを設定することもできます。構成オプションの一覧については、資料を参照してください。

    /* Sent when a download task that has completed a download.  The delegate should
     * copy or move the file at the given location to a new location as it will be
     * removed when the delegate message returns. URLSession:task:didCompleteWithError: will
     * still be called.
     */
    - (void)URLSession:(NSURLSession *)session downloadTask:(NSURLSessionDownloadTask *)downloadTask
                                  didFinishDownloadingToURL:(NSURL *)location;

    /* Sent periodically to notify the delegate of download progress. */
    - (void)URLSession:(NSURLSession *)session downloadTask:(NSURLSessionDownloadTask *)downloadTask
                                               didWriteData:(int64_t)bytesWritten
                                          totalBytesWritten:(int64_t)totalBytesWritten
                                  totalBytesExpectedToWrite:(int64_t)totalBytesExpectedToWrite;

    /* Sent when a download has been resumed. If a download failed with an
     * error, the -userInfo dictionary of the error will contain an
     * NSURLSessionDownloadTaskResumeData key, whose value is the resume
     * data.
     */
    - (void)URLSession:(NSURLSession *)session downloadTask:(NSURLSessionDownloadTask *)downloadTask
                                          didResumeAtOffset:(int64_t)fileOffset
                                         expectedTotalBytes:(int64_t)expectedTotalBytes;

