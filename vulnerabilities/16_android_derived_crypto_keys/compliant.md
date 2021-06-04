
The following are the rules which should be followed while using
encryption:

- If AES encryption is used, always pair it with CBC (Cipher Block Chaining)
- Never use just AES as encryption because it defaults to AES/ECB (Electronic Codebook)
- Always use padding with the encryption, for example, AES/CBC/PKCS7 is stronger than just AES/CBC
- Never use older algorithm like DES (Data Encryption Standard)
- Assume that the network layer is not secure and may potentially be hostile and eavesdropping.
- Enforce the use of SSL/TLS for all transport channels in which
  sensitive information, session tokens, or other sensitive data is
  going to be communicated to a backend API or web service.
- Remember to account for outside entities like third-party analytics,
  social networks, etc. and use their SSL versions even when an
  application runs a routine via the browser/webkit. Mixed SSL
  sessions should be avoided and may expose the user's session ID.
- Use strong, industry standard encryption algorithms and appropriate
  key lengths.
- Use certificates signed by a trusted CA provider.
- Never allow self-signed certificates, and consider certificate
  pinning for security conscious applications.
- Do not disable or ignore SSL chain verification.
- Only establish a secure connection after verifying the identity of
  the endpoint server with trusted certificates in the key chain.
- Alert users through the UI if an invalid certificate is detected.
- Do not send sensitive data over alternate channels, such as SMS,
  MMS, or notifications.
