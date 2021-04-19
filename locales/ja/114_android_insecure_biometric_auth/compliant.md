
1.  Create the Android keystore key with `setUserAuthenticationRequired` and
    `setInvalidatedByBiometricEnrollment` set to `true`. Additionally,
    `setUserAuthenticationParameters`'s timeout param should be set to `0`
2.  Initialize cipher object with keystore key created above.
3.  Create `BiometricPrompt.CryptoObject` using cipher object from previous step.
4.  Implement `BiometricPrompt.AuthenticationCallback.onAuthenticationSucceeded`
    callback which will retrieve cipher object from the parameter and use this cipher
    object to decrypt some other crucial data such as session key, or a secondary
    symmetric key which will be used to decrypt application data.
5.  Call `BiometricPrompt.authenticate` function with crypto object and callbacks
    created in steps 3 and 4.

Here is a sample implementation:

    biometricPrompt = new BiometricPrompt(MyActivity.this, executor, new BiometricPrompt.AuthenticationCallback() {
        @Override
        public void onAuthenticationSucceeded(BiometricPrompt.AuthenticationResult result) {
            super.onAuthenticationSucceeded(result);
            BiometricPrompt.CryptoObject cryptoObject = result.getCryptoObject();

            // Use cryptoObject for grant access logic
            Cipher cipher = cryptoObject.getCipher();
            cryptedInfo = cipher.doFinal(info);
            accessGranted(cryptedInfo);
        }
        ...
    });
    ...
    KeyGenParameterSpec keyGenParameterSpec = new KeyGenParameterSpec.Builder(KEY_NAME, KeyProperties.PURPOSE_ENCRYPT | KeyProperties.PURPOSE_DECRYPT)
        .setUserAuthenticationRequired(true)
        .setInvalidatedByBiometricEnrollment(true)
        .setUserAuthenticationParameters(0, KeyProperties.AUTH_BIOMETRIC_STRONG)
        .build()

    KeyGenerator keyGenerator = KeyGenerator.getInstance(algorithm, "AndroidKeyStore");
    keyGenerator.init(keyGenParameterSpec);
    keyGenerator.generateKey();
    ...
    Cipher cipher = Cipher.getInstance(transformation);
    SecretKey secretKey = ((SecretKey) keyStore.getKey(KEY_NAME, password));
    cipher.init(mode, secretKey);
    biometricPrompt.authenticate(promptInfo, new BiometricPrompt.CryptoObject(cipher));

