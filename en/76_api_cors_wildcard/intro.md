
Cross Origin Resource Sharing (CORS) is a specification that allows cross domain
communication in a web browser. It works by defining new HTTP headers that describe
the origins that are allowed cross domain information transmission, thus allowing
restricted resources (e.g. fonts) on a web page to be requested from another
domain outside the domain from which the first resource was served.

`Access-Control-Allow-Origin` header should be never set to `*` especially if the resource
contains sensitive information. It should be set to allow requests only from the
domains that are trusted.
