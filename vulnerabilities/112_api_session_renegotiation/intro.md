
The attack exploits TLS's renegotiation feature, which allows a client and
server who already have a TLS connection to negotiate new parameters,
generate new keys, etc. Renegotiation is carried out in the existing TLS
connection, with the new handshake packets being encrypted along with
application packets. The difficulty is that they're not otherwise tied to
the channel, which gives the attacker a window.