
Certificate Pinning can be done with these two options:

You can
1. pin the certificate or
2. pin the public key

If you choose public keys, you have two additional choices:
- pin the `subjectPublicKeyInfo` or
- pin one of the concrete types such as `RSAPublicKey` or `DSAPublicKey`.

The three choices are explained below in more detail. I would encourage you to pin the subjectPublicKeyInfo because it has the public parameters (such as {e,n} for an RSA public key) and contextual information such as an algorithm and OID. The context will help you keep your bearings at times, and the figure to the right shows the additional information available.

### Certificate

The certificate is easiest to pin. You can fetch the certificate out of band for the website, have the IT folks email your company certificate to you, use openssl s_client to retrieve the certificate etc. At runtime, you retrieve the website or server's certificate in the callback. Within the callback, you compare the retrieved certificate with the certificate embedded within the program. If the comparison fails, then fail the method or function. There is a downside to pinning a certificate. If the site rotates its certificate on a regular basis, then your application would need to be updated regularly. For example, Google rotates its certificates, so you will need to update your application about once a month (if it depended on Google services). Even though Google rotates its certificates, the underlying public keys (within the certificate) remain static.

### Public Key

Public key pinning is more flexible but a little trickier due to the extra steps necessary to extract the public key from a certificate. As with a certificate, the program checks the extracted public key with its embedded copy of the public key. There are two downsides to public key pinning. First, it's harder to work with keys (versus certificates) since you must extract the key from the certificate. Extraction is a minor inconvenience in Java and .Net, buts it's uncomfortable in Cocoa/CocoaTouch and OpenSSL. Second, the key is static and may violate key rotation policies.

### Hashing

While the three choices above used DER encoding, its also acceptable to use a hash of the information. In fact, the original sample programs were written using digested certificates and public keys. The samples were changed to allow a programmer to inspect the objects with tools like dumpasn1 and other ASN.1 decoders.

Hashing also provides three additional benefits. First, hashing allows you to anonymize a certificate or public key. This might be important if you application is concerned about leaking information during decompilation and re-engineering. Second, a digested certificate fingerprint is often available as a native API for many libraries, so its convenient to use. Finally, an  organization might want to supply a reserve (or back-up) identity in  case the primary identity is compromised. Hashing ensures your adversaries  do not see the reserved certificate or public key in advance of its use. In fact,  Google's IETF draft websec-key-pinning uses the technique.

