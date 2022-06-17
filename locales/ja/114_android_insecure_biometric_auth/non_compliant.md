
脆弱性のある実装には、通常、以下に示すようなコードが含まれています:

    biometricPrompt = new BiometricPrompt(MyActivity.this, executor, new BiometricPrompt.AuthenticationCallback() {
        @Override
        public void onAuthenticationSucceeded(BiometricPrompt.AuthenticationResult result) {
            super.onAuthenticationSucceeded(result);
            accessGranted();
        }
        ...
    });
    ...
    biometricPrompt.authenticate(promptInfo);

The code listed above does not use the CryptoObject passed in the
`AuthenticationResult`, instead it just assumes that authentication was successful
since `onAuthenticationSucceeded` was called.
