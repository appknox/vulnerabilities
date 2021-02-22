
When making an SSL connection, app will only trust the server if the 
server can provide a valid certificate that is signed by one of the 
trusted Certificate Authorities that come pre-installed in the device.
An attacker can abuse this mechanism by installing a malicious root 
CA certificate to user devices so the device will trust all certificates 
that are signed by the attacker. Therefore relying on the certificates 
received from servers alone cannot guarantee the authenticity of the 
server, and it is vulnerable to a potential man-in-the-middle attack.

An app can protect itself from fraudulently issued certificates by a 
technique known as Pinning. Certificate Pinning is the process of 
associating a host with their expected X509 certificate or public key. 
A list of trustful certificates can be pinned to the app during 
development, and use them to compare against the server certificates 
during runtime. This enforcement ensures that the app is communicating 
only to the dedicated trustful servers.