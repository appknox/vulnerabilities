
The predominant Android cryptographic security provider API defaults to
using an insecure AES encryption method: ECB block cipher mode for AES
encryption. Android's default cryptographic security provider (since
version 2.1) is BouncyCastle.

Note that Java also selects ECB as a default value when only the AES
encryption method is chosen. So, this rule also applies to Java, but for
Java's different default cryptographic security provider. Oracle Java's
default cryptographic security provider is SunJCE.

Default behaviors of cryptographic libraries used in Android systems
often do not use recommended practices. For example, the predominant
Android Java security provider API defaults to using an insecure AES
encryption method: ECB block cipher mode for AES encryption. Extensive
app testing by Egele 2013 has shown that the following 6 rules are
often not followed, resulting in 88 percent of apps with cryptographic APIs on
Google Play making at least one mistake.

Six common cryptography rules that were tested:

1.  Do not use ECB mode for encryption.
2.  Do not use a non-random IV for CBC encryption.
3.  Do not use constant encryption keys.
4.  Do not use constant salts for PBE.
5.  Do not use fewer than 1,000 iterations for PBE.
6.  Do not use static seeds to seed SecureRandom().

