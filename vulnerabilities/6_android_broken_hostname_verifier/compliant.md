
The code example shows how to verify hostname using a
wrapper `HostnameVerifier` which also checks for custom loaded certificates

    public HostnameVerifier wrapHostnameVerifier(final HostnameVerifier defaultVerifier) {
        if (defaultVerifier == null)
            throw new IllegalArgumentException("The default verifier may not be null");

        return new SecuringHostnameVerifier(defaultVerifier);
    }

    class SecuringHostnameVerifier implements HostnameVerifier {
        private HostnameVerifier defaultVerifier;

        public MemorizingHostnameVerifier(HostnameVerifier wrapped) {
            defaultVerifier = wrapped;
        }

        @Override
        public boolean verify(String hostname, SSLSession session) {
            Log.d("log", "hostname verifier for " + hostname + ", trying default verifier first");
            // if the default verifier accepts the hostname, we are done
            if (defaultVerifier.verify(hostname, session)) {
                Log.d("log", "default verifier accepted " + hostname);
                return true;
            }
            // otherwise, we check if the hostname is an alias for this cert in our keystore
            try {
                X509Certificate cert = (X509Certificate)session.getPeerCertificates()[0];
                if (cert.equals(appKeyStore.getCertificate(hostname.toLowerCase(Locale.US)))) {
                    Log.d("log", "certificate for " + hostname + " is in keystore. accepting.");
                    return true;
                } else {
                    Log.d("log", "server " + hostname + " provided wrong certificate.");
                    return false;
                }
            } catch (Exception e) {
                e.printStackTrace();
                return false;
            }
        }
    }

