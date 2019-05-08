
Command injection is an attack in which the attacker attempts execution of arbitrary commands
on the host operating system via a vulnerable application. This attack differs from Code Injection,
in that code injection allows the attacker to add his own code that is then executed by the application.
In Code Injection, the attacker extends the default functionality of the application
without the necessity of executing system commands.

Command injection attacks are possible when an application passes unsafe user supplied data
(forms, cookies, HTTP headers etc.) to a system shell. The attacker-supplied
operating system commands are usually executed with the privileges of the vulnerable application.
Command injection attacks are possible largely due to insufficient input validation.
