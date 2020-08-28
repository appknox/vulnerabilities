
Typically, modern TLS servers support old protocol versions and weak
cryptographic algorithms for backward compatibility with
older client and servers. One of the simplest and most reliable
mitigation for downgrade attacks which can be easily applied to modern
TLS implementations is just disabling insecure protocol versions and algorithms.
But this may cost too much because of compatibility issues.