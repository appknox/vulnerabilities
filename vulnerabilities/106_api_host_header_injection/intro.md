
A web server commonly hosts several web applications on the same IP address,
referring to each application via the virtual host.

In an incoming HTTP request, web servers often dispatch the request to the
target virtual host based on the value supplied in the Host header.
Without proper validation of the header value, the attacker can supply invalid
input to cause the web server to:

- dispatch requests to the first virtual host on the list
- cause a redirect to an attacker-controlled domain
- perform web cache poisoning
- manipulate password reset functionality

