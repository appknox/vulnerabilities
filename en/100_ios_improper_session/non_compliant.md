
1) The application generates an access token based on the username, ID or cryptographically insecure algorithm which can be easily enumerated.

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: testuser
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: 560192
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

    POST /api/sessions HTTP/1.1
    Host: site.com
    Content-Type: application/x-www-form-urlencoded; charset=utf-8
    Accept-Language: en-us
    Access-Token: 5d9c68c6c50ed3d02a2fcf54f63993b6
    Connection: close
    Accept: */*
    User-Agent: Chrome/5.5.1 (iPhone/10.0.2; iPhone OS; en_IN;)
    Content-Length: 40

2) The application does not invalidate the session token at the backend. So, even after the use logs out, it is possible to make successful requests using the expired token to access the resources of the user.

3) In case of critical functionalities, the application should reject if the requests are replayed. For example, if a request is made to the server to recharge or pay the amount, on repeating the same request, the server should reject the replayed request.

4) Session tokens does not have an expiry and they are valid for an indefinite time.

