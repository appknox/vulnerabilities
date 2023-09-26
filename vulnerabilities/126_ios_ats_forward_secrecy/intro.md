
The "NSExceptionRequiresForwardSecrecy" key is part of the App Transport Security (ATS)
configuration in iOS apps. It indicates whether to override the perfect forward secrecy (PFS)
requirement. The default value is set to true, which limits the accepted ciphers to those
that support PFS through Elliptic Curve Diffie-Hellman Ephemeral (ECDHE) key exchange. PFS
ensures that even if an attacker obtains the private key used for encryption, they cannot
retroactively decrypt past communication sessions.
