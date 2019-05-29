
`NSURLConnection` is a commonly used API for establishing network 
connections with the server. However, it has been replaced by
`NSURLSession` & deprecated by Apple starting iOS 9.0. The most 
notable improvement `NSURLSession` provides over `NSURLConnection` 
is the ability to configure per-session cache, protocol, cookie, 
and credential policies, rather than sharing them across the app. 
It also handles the authentication challenge issued by the 
server in a more appropriate way.