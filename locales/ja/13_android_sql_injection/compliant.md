
入力検証は、適切なクエリ構築の前提条件です。 この準拠のソリューションは、ユーザー名とパスワードの引数の長さを検証します。 また、java.sql.Statement の代わりに java.sql.PreparedStatement も使用します。

    class Login {
        public void doPrivilegedAction(String username, String password) throws SQLException {

            // ensure that the length of username and password is legitimate
            if ((username.length() >= 8) || (password.length() >= 20)) {
                // handle error
                ...
            }

            DriverManager.registerDriver(new com.microsoft.jdbc.sqlserver.SQLServerDriver());
            Connection connection = DriverManager.getConnection("jdbc:microsoft:sqlserver://:1433", "", "");

            if (connection != null) {
                String sql = "select * from db_user where username=? and password=?";

                // use PreparedStatement for type enforcement
                PreparedStatement stmt = connection.prepareStatement(sql);
                stmt.setString(1, username);
                stmt.setString(2, password);
                ResultSet rs = stmt.executeQuery();

                if (!rs.next()) {
                    throw new SecurityException("User name or Password incorrect");
                }
                // we've authenticated; proceed
                ...
            }
        }
    }

