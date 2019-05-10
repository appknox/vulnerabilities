
SSLまたはTLSでHTTPを使用してインターネットに接続するか、適切な証明書を使用しないと、ユーザーに気づかれずに攻撃者が簡単に接続を盗聴できます。

    String link = "http://www.google.com";
    URL url = new URL(link);

    HttpURLConnection conn = (HttpURLConnection) url.openConnection();
    conn.connect();

    InputStream is = conn.getInputStream();
    BufferedReader reader = new BufferedReader(new InputStreamReader(is, "UTF-8"));
    String webPage = "", data="";
    while ((data = reader.readLine()) != null) {
       webPage += data;
    }

ユーザーに誰かが接続を盗聴していることさえ気づかせずに、攻撃者はMITM攻撃を行うことができます。
