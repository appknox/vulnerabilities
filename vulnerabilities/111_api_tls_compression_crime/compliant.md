
CRIME can be defeated by preventing the use of compression, and disabling the
compression of SPDY requests, or by the website preventing the use of
data compression on such transactions using the protocol negotiation features
of the TLS protocol. As detailed in The Transport Layer Security (TLS)
Protocol Version 1.2, the client sends a list of compression algorithms
in its ClientHello message, and the server picks one of them and sends it
back in its ServerHello message. The server can only choose a compression
method the client has offered, so if the client only offers
'none' (no compression), the data will not be compressed.

Similarly, since 'no compression' must be allowed by all TLS clients, a
 server can always refuse to use compression.