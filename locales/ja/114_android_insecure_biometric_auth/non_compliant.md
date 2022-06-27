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

上記のコードでは、`AuthenticationResult`で渡されたCryptoObjectは使用しません。
代わりに、`onAuthenticationSucceeded` が呼び出されたので、認証が成功したと仮定しています。