
To work with legacy servers, many TLS clients implement a downgrade path,
in a first handshake attempt, offer the highest protocol version supported by
the client; if this handshake fails, then retry (possibly repeatedly) with
earlier protocol versions.
