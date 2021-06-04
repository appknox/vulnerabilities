
Ensure you have no vulnerable applications on your SSL stack.
If you do have any vulnerable applications, make sure that you applied the
related fix released by the vendor (if any available).

RSA encryption modes are so risky that the only safe course of action is to
disable them. These encryption modes also lack forward secrecy.
Thus we strongly recommend, as a preventive measure, to disable all the
TLS_RSA cipher suites on your SSL stack (except for the ones that have
DHE or ECDHE in their name).
