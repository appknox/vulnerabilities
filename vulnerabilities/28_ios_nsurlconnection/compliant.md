
It is advisable to use `NSURLSession` for all types of network connections
instead of `NSURLConnection` because Apple can stop supporting
`NSURLConnection` anytime in near future.

`NSURLSession` is the key object responsible for sending and receiving
HTTP requests. It can be created via `NSURLSessionConfiguration`, which
comes in three flavors:

`defaultSessionConfiguration`: Creates a default configuration object
that uses the disk-persisted global cache, credential and cookie storage
objects.

`ephemeralSessionConfiguration`: Similar to the default configuration,
except that all session-related data is stored in memory. Think of this
as a "private" session.

`backgroundSessionConfiguration`: Lets the session perform upload or
download tasks in the background. Transfers continue even when the app
itself is suspended or terminated.

NSURLSessionConfiguration also lets you configure session properties
such as timeout values, caching policies and additional HTTP headers.
Refer to the documentation for a full list of configuration options.

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

