Statement st = conn.createStatement();
String query = 'SELECT * FROM  User where userId='' + user + ''';
out.println('Query : ' + query);
System.out.printf(query);
ResultSet res = st.executeQuery(query);