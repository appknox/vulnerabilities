
**For passwords**, deliberately slow hash constructions, such as scrypt, bcrypt and
PBKDF2 should be used. Simple salted SHA-2 is not good enough because, like most
general purpose hashes, it is fast. ([How to securely hash passwords](https://security.stackexchange.com/questions/211/how-to-securely-hash-passwords))

**For file integrity**, the current best solution is SHA-2 (SHA-256). Once SHA-3 gets
standardized it will be a good choice too.
