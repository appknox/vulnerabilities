
Altough JSON is intended as a data serialization format, its design as a
non-strict subset of the JavaScript scripting language poses several security
concerns, which are centered on the use of a JavaScript interpreter to execute
JSON text dynamically as embedded JavaScript. This easy and popular but risky
technique exploits JSON's compatibility with the JavaScript `eval()` function.
It is possible that the JSON parser will reach depth limit and crash,
resulting in a successful overflow of the JSON parsers depth limit, leading
to a DoS vulnerability.
