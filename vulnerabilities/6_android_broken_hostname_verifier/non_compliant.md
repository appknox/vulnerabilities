
The following code inherits `javax.net.ssl.SSLContext`:

    public void HostnameVerifier() {
        HostnameVerifier hv = new HostnameVerifier() {
            @Override
            public boolean verify(String hostname, SSLSession session) {
                // Always return true -> Accept any host names
                return true;
            }
        };
    }

`HostnameVerifier` will always return true without checking the contents
or verifying the hostname
