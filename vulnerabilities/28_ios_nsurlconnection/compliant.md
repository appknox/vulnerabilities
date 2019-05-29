
It is advisable to use [`NSURLSession`](https://developer.apple.com/documentation/foundation/nsurlsession) 
for all types of network connections instead of [`NSURLConnection`](https://developer.apple.com/documentation/foundation/nsurlconnection) 
because Apple can stop supporting `NSURLConnection` anytime in near future.


    let url = NSURL(string:"https://www.example.com")
    let request = NSURLRequest(URL: url)
    let session = NSURLSession.sharedSession()

    let task = session.dataTaskWithRequest(request) {
        (data: NSData?, response: NSURLResponse?, error: NSError?) -> Void in
        if (error == nil) {
            // process data
        }
    }
    task.resume()


`sharedSession` used in the above snippet is a shared singleton session 
object that gives a reasonable default behavior for creating tasks. 
For per session customizations such as timeout values, caching policies 
and additional HTTP headers, `NSURLSessionConfiguration` can be used. 
There are three factory constructors for instantiating standard 
configurations:

1. `defaultSessionConfiguration`: Creates a default configuration object
that uses the disk-persisted global cache, credential and cookie storage
objects.
2. `ephemeralSessionConfiguration`: Similar to the default configuration,
except that all session-related data is stored in memory. Think of this
as a "private" session.
3. `backgroundSessionConfiguration`: Lets the session perform upload or
download tasks in the background. Transfers continue even when the app
itself is suspended or terminated.

Example session using default configuration:


    let url = NSURL(string:"https://www.example.com")
    let request = NSURLRequest(URL: url)
    request.addValue("application/json", forHTTPHeaderField: "Content-Type")

    let defaultConfigObject = NSURLSessionConfiguration.defaultSessionConfiguration()
    defaultConfigObject.timeoutIntervalForRequest = 10

    let session = NSURLSession(configuration: defaultConfigObject, delegate: self, delegateQueue: NSOperationQueue.mainQueue())

    let task = session.dataTaskWithRequest(request) {
        (data: NSData?, response: NSURLResponse?, error: NSError?) -> Void in
        if (error == nil) {
            // process data
        }
    }
    task.resume()
