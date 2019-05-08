
Insecure Direct Object References occur when an application provides direct access to objects based on user-supplied input.
As a result of this vulnerability, attackers can bypass authorisation and access resources in the system directly, by modifying
the value of a parameter used to point to an object. Such resources can be database entries belonging to other users, files in the system, or others.
This is caused by the fact that the application takes user supplied input and uses it to retrieve an object without performing sufficient authorisation checks.
