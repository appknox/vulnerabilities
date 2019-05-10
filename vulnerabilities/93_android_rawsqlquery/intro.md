
Sql injection is possible because we use quotation marks to delimit strings and also to be parts of strings, making it impossible to interpret them sometimes. If we had delimiters that could not be used in string data, sql injection never would have happened. Solving the delimiter problem eliminates the sql injection problem. Structure queries do that.

Prepared statements are resilient against SQL injection, because parameter values, which are transmitted later using a different protocol, need not be correctly escaped. If the original statement template is not derived from external input, SQL injection cannot occur.
