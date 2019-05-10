
**For passwords**, deliberately slow hash constructions such as scrypt, bcrypt and
PBKDF2 should be used. Simple salted SHA2 is not good enough because, like most
general purpose hashes, it is fast.

**For file integrity**, the current best solution is SHA-2 (SHA-256). SHA-3 will also be
a good choice once it gets standardised.
