
`NSURLConnection` is the most common API used for establishing network
connections with the server. However, it has been replaced by
`NSURLSession` & deprecated by Apple starting iOS 9.0. `NSURLSession`
provides support for configuring per-session cache, protocol, cookie,
and credential policies, rather than sharing them across the app which
handles authentication challenge in a more appropriate way.
