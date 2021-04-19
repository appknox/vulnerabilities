
The vulnerable implementations usually included something similar to the code shown
below:

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
