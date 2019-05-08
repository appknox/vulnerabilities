
この非準拠のコード例は、SQLインジェクションに対して脆弱なJDBCコードを示しています。 SQLステートメントは、入力引数を受け入れます。

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

攻撃者が有効なユーザー名 securecoding を入力し、パスワード引数に 'OR username =' 
securecodingと入力すると、SQL文は、username '' OR 
username = 'securecoding'およびpassword = ''のdb
 \ _ userから\ *を選択し、結果的にログインパスワードチェックをバイパスします。
同様に、ユーザー 'OR' 1 '=' 1の入力は、
ユーザー名とパスワードの両方のチェックをバイパスし、攻撃者に無制限アクセスを許可します。
