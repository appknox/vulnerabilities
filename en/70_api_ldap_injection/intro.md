
LDAP injection is an attack used to exploit web based applications that construct
LDAP statements based on user input. When an application fails to properly
sanitize user input, it is possible to modify LDAP statements using a local proxy.
This could result in the execution of arbitrary commands such as granting permissions
to unauthorized queries, and content modification inside the LDAP tree. The same
advanced exploitation techniques available in SQL injection can be similarly
applied in LDAP injection.
