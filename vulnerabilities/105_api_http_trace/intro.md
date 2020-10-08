
The HTTP TRACE method is normally used to return the full HTTP request back to
the requesting client for proxy-debugging purposes.
An attacker can create a webpage using XMLHTTP, ActiveX, or XMLDOM to
cause a client to issue a TRACE request and capture the client's cookies.
This effectively results in a Cross-Site Scripting attack.
