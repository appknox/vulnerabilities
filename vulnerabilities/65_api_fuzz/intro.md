
This issue is not specific to a certain kind of vulnerabilities. It can be raised as
a result of many different types of attacks and might indicate some server-side
fault that may lead to further vulnerabilities

When an attacker explores a web site looking for vulnerabilities, the amount of
information that the site provides is crucial to the eventual success or failure
of any attempted attacks. If the application shows the attacker a stack trace,
it relinquishes information that makes the attacker's job significantly easier.
For example, a stack trace might show the attacker a malformed SQL query string,
the type of database being used, and the version of the application container.
This information enables the attacker to target known vulnerabilities in these components.

The application configuration should specify a default error page in order to
guarantee that the application will never leak error messages to an attacker.
Handling standard HTTP error codes is useful and user-friendly in addition to
being a good security practice, and a good configuration will also define a
last-chance error handler that catches any exception that could possibly be
thrown by the application.
