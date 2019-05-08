
A buffer overflow occurs when a program attempts to put more data in a buffer than
it can hold or when a program attempts to put data in a memory area past a buffer.
In this case, a buffer is a sequential section of memory allocated to contain anything
from a character string to an array of integers. Writing outside the bounds of a
block of allocated memory can corrupt data, crash the program, or cause the execution of malicious code.

Attackers use buffer overflows to corrupt the execution stack of a web application.
By sending carefully crafted input to a web application, an attacker can cause the
web application to execute arbitrary code.

Buffer overflow flaws can be present in both the web server or application server
products that serve the static and dynamic aspects of the site, or the web application itself.
