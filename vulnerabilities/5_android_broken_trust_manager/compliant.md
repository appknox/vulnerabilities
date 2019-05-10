
The compliant solution is given below which shows how to solve the issue
with the non compliant code:

    public void checkCertTrusted(X509Certificate[] chain, String authType, boolean isServer) throws CertificateException {
        try {
            if (isServer)
                appTrustManager.checkServerTrusted(chain, authType);
            else
                appTrustManager.checkClientTrusted(chain, authType);
        } catch (CertificateException ae) {
            // if the cert is stored in our appTrustManager, we ignore expiredness
            if (isExpiredException(ae)) {
                Log.i("log", "accepting expired certificate from keystore");
                return;
            }
            if (isCertKnown(chain[0])) {
                Log.i("log", "accepting cert already stored in keystore");
                return;
            }
            try {
                if (defaultTrustManager == null)
                    throw ae;
                Log.d("log", "trying defaultTrustManager");
                if (isServer)
                    defaultTrustManager.checkServerTrusted(chain, authType);
                else
                    defaultTrustManager.checkClientTrusted(chain, authType);
            } catch (CertificateException e) {
                Log.d("log", "defaultTrustManager failed: " + e);
                interactCert(chain, authType, e);
            }
        }
    }

    public void checkTrustManager() throws IOException, KeyManagementException, NoSuchAlgorithmException {
        TrustManager tm = new X509TrustManager() {

            @Override
            public void checkClientTrusted(X509Certificate[] chain,
                    String authType) throws CertificateException {
                checkCertTrusted(chain, authType, false);
            }

            @Override
            public void checkServerTrusted(X509Certificate[] chain,
                    String authType) throws CertificateException {
                checkCertTrusted(chain, authType, false);
            }

            @Override
            public X509Certificate[] getAcceptedIssuers() {
                return defaultTrustManager.getAcceptedIssuers();
            }
        };
    }

The method `checkCertTrusted()` gives an idea about how to solve this
issue. If a custom keystore is being used to load certificates then we
need to define and do a failsafe load of those certificates.
