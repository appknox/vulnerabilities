
1.  Android keystore keyを `setUserAuthenticationRequired`と
    `setInvalidatedByBiometricEnrollment`を`true`にして作成します. さらに、
    `setUserAuthenticationParameters`の timeout param を `0`に設定します。
2.  上記で作成したkeystore keyでcipherオブジェクトを初期化します。
3.  前項のcipherオブジェクトを使用して `BiometricPrompt.CryptoObject`を作成します。
4.  パラメータからcipherオブジェクトを取得し、このcipherオブジェクトを使用してsession keyやアプリケーションデータの復号に使用されるsecondary symmetric keyなど、他の重要なデータを復号化する `BiometricPrompt.AuthenticationCallback.onAuthenticationSucceeded`コールバックを実装します。
5.  手順3.4で作成したcryptoオブジェクトとコールバックを使用して、 `BiometricPrompt.authenticate` 関数を呼び出します。

以下は実装のサンプルです:

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

