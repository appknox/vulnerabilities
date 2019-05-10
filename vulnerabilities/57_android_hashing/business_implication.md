
Using salted MD5 for passwords is a bad idea. Not because of MD5's cryptographic
weaknesses, but because it is fast. This means that an attacker can try billions
of candidate passwords per second on a single GPU. (See [Dangers of Weak Hashes](https://www.sans.org/reading-room/whitepapers/authentication/dangers-weak-hashes-34412))

Using MD5 for file integrity may or may not be a practical problem, depending on
the exact usage scenario. The attacks against MD5 are collision attacks, not
pre-image attacks. This means an attacker can produce two files with the same
hash, if they have control over both of them. But they can't match the hash of
an existing file they didn't influence.

Although SHA1 remains the world's widely used hashing algorithm, with Git and
GnuPG relying on it for data integrity, it was recently
[proven](https://shattered.io/static/shattered.pdf) to be susceptible to collision attacks.
