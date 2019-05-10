
An integer overflow occurs when the result of an arithmetic operation exceeds the maximum size
of the integer data type used to store it. When an integer overflow occurs, the calculated value
will wrapped around the maximum value allowed by the data structure and start from the minimum value.

Attackers use integer overflows to corrupt the data stack of the web application.
By sending carefully crafted input to the server, an attacker can cause the data corruption.
Attackers can use these defects to influence the value of variables in ways that the application is not meant
to.
