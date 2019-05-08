
The Cross-Site Tracing (XST) attack makes use of Cross-site Scripting (XSS)
and the TRACE or TRACK HTTP methods. TRACE allows the client to see what is
being received at the other end of the request chain and use that data for
testing or diagnostic information. The TRACK method works in the same way but
is specific to Microsoft's IIS web server. XST could be used as a method to
steal user's cookies via Cross-site Scripting (XSS) even if the cookie has the
`HttpOnly` flag set and/or exposes the user's Authorization header.

Modern browsers now prevent TRACE requests being made via JavaScript, however,
other ways of sending TRACE requests with browsers have been discovered, such as using Java.
