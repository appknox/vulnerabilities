
Example code which is using deprecated `NSURLConnection` API:

    let queue = NSOperationQueue.mainQueue()
    let url = NSURL(string: "https://www.example.com")!
    let request = NSURLRequest(URL: url)

    NSURLConnection.sendAsynchronousRequest(request, queue: queue) {
        (response: NSURLResponse?, data: NSData?, error: NSError?) in
        if (error == nil) {
            // process data
        }
    }
