
Android applications built with the Cordova framework use a WebView
component to display content. Cordova applications can specify a
whitelist of URLs which the application will be allowed to display, or
to communicate with via XMLHttpRequest. This whitelist, however, is not
used by the WebView component when it is directed via JavaScript to
communicate over non-http channels.

Specifically, it can be possible to open a WebSocket connection from the
application JavaScript which will connect to any reachable server on the
Internet. If an attacker is able to execute arbitrary JavaScript within
the application, then that attacker can cause a connection to be opened
to any server, bypassing the HTTP whitelist.

This is a limitation of the hybrid app architecture on Android in
general, and not specific to Apache Cordova.
