
Android apps contain a lot of user information which also includes some
sensitive ones such as username, password, email id, banking details, etc. This
information is stored by the app in SQLite database in various tables using
diﬀerent attributes. To keep them secure, an app is expected to keep the
information in secure and encrypted format.

Whenever an app creates a database, by default it is saved
in a location: `/data/data/app name/database/`. This location is private to an
app and not accessible to the user or other apps. To share data stored in SQLite
database, an app can use Content Provider

However, these databases don't have any built-in support for encryption and
hence, all the information is stored in plain-text format in these files
