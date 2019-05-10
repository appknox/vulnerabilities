
On Apple platforms, a networking security feature called App Transport
Security (ATS) is available to apps and app extensions, and is enabled
by default. It improves privacy and data integrity by ensuring your
app's network connections employ only industry-standard protocols and
ciphers without known weaknesses. This helps instill user trust that
your app does not accidentally leak transmitted data to malicious
parties.

By configuring this key's value in your app's `Info.plist` file, you can
customize the security of your network connections in a variety of ways.
You can:

- Allow insecure communication with particular servers
- Allow insecure loads for web views or for media, while maintaining ATS protections elsewhere in your app
- Enable new security features such as Certificate Transparency

