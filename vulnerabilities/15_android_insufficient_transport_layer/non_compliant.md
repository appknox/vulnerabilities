
Using HTTP with SSL or TLS to connect to internet, or without a proper
certificate the connection can be easily eavesdropped by attacker
without the knowledge of the user.

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

An attacker can perform a MITM attack and the user wouldn't even know
that someone is eavesdropping the connection.
