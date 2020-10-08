
OpenSSL’s flaw with ChangeCipherSpec processings makes it possible for
malicious third parties to intermediate specific communication.
Through this bug, attackers are able to enforce OpenSSL servers and clients
to use weak key materials.

There are risks of tampering with and exploits on contents and authentication
information over encrypted communication, when the software uses
the affected version of OpenSSL.
