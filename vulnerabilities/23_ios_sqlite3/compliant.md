
It is suggested to use custom encryption while storing data in SQLite
databases.

SQLite engine writes the data into Write Ahead Log (WAL) before storing
it in the actual database file. Using WAL, there is a possibility to
recover the deleted data from the database file. Hence, before deleting
any SQLite record, always overwrite it with some junk data so that it
can't be read even if someone tries to recover it.
