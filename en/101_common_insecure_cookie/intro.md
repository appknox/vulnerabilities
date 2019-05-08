
Cookies are often a key attack vector for malicious users (typically targeting other users) and the application should always take due diligence to protect cookies. Cookies generally are very common and widely used in browser world, mainly for Session Management, User preferences and state etc. Cookie is a small piece of data with some attributes sent by servers. This is stored by browsers and shared with server in the subsequent requests.

If cookie not marked as secure then it can be transmitted over a HTTP connection, therefore if this cookie is important (such as a session cookie), an attacker might intercept it and hijack a victim's session. If the attacker can carry out a man-in-the-middle attack, he/she can force the victim to make an HTTP request to steal the cookie.
and if it is not marked as HTTPOnly, during a cross-site scripting attack, an attacker might easily access cookies and hijack the victim's session.
