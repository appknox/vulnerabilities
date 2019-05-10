
This non-compliant code example shows JDBC code that is vulnerable to
SQL injection. The SQL statement SQL accepts unsanitized input
arguments.

    class Login {
        public void doPrivilegedAction(String username, String password) throws SQLException {

            DriverManager.registerDriver(new com.microsoft.jdbc.sqlserver.SQLServerDriver());
            Connection connection = DriverManager.getConnection(
                "jdbc:microsoft:sqlserver://<HOST>:1433", "<UID>", "<PWD>");

            if (connection != null) {
                String sql = "select * from db_user where username = '" + username +
                    "' and password = '" + password + "'";

                Statement stmt = connection.createStatement();
                ResultSet rs = stmt.executeQuery(sql);
                if (!rs.next()) {
                    throw new SecurityException("User name or Password incorrect");
                }
                // Authenticated; proceed
            }
        }
        ...

If the attacker enters a valid user name securecoding and enters 'OR
username = 'securecoding for the password argument, the SQL statement
evaluates to select \* from db\_user where username = '' OR username =
'securecoding' and password='', consequently bypassing the login
password check. Similarly, an input ofsomeuser' OR '1' = '1 would bypass
both the user name and password checks, granting the attacker
unrestricted access.
