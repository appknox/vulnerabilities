
Using the CCCryptor, one can use common sounding functions such as
`CCCryptorCreate`, `CCCryptorUpdate`, `CCCryptorFinal` (or simply `CCCrypt()`
one-shot function) to perform symmetric encryption using different
algorithms like AES, 3DES and hardcore security ciphers like RC4, DES,
etc.

Apple supports ECB and CBC mode for their ciphers, and fortunately a
developer really needs to explicitly prove stupidity by using ECB since
APIs default to CBC, the Cipher Block Chaining mode. What could possibly
go wrong? Right, there is some minor thing that is called the "IV".
Apple supposedly translated the acronym IV to "Ignorance Vector" when
writing their Common Crypto API man-pages, but we should read
"Initialization Vector" - used to initialize the very first block of
cipher text.
