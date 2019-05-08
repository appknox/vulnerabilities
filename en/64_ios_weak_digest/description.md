
Using salted MD5 for passwords should be avoided, not because of its cryptographic
weaknesses, but because it is fast. An attacker can try billions of candidate passwords
per second on a single GPU.

Using MD5 for file integrity may or may not be a practical problem, depending on
the exact usage scenario. The attacks against MD5 are collision attacks, not
pre-image attacks which means an attacker can produce two files with the same
hash, if they have control over both of them. However, they cannot match the hash of
an existing file they didn't influence.

Although SHA1 remains the world's widely used hashing algorithm with Git and
GnuPG relying on it for data integrity, it has [also been proven](https://shattered.io/static/shattered.pdf)
to be susceptible to collision attacks.
