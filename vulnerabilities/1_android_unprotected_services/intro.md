
[Chin, et al.](https://www.securecoding.cert.org/confluence/display/java/AA.+References#AA.References-Chin11)
say: "If a Service is exported and not
protected with strong permissions, then any application can start and
bind to the Service. Depending on the duties of a particular Service, it
may leak information or perform unauthorized tasks. Services sometimes
maintain singleton application state, which could be corrupted."

To guard against such eventualities, an exported service should always
be protected with strong permissions.
