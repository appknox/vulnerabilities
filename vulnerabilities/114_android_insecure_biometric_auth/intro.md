
The parameters of Biometric API `authenticate` method include a `CryptoObject` which
contains a reference to the Keystore entry that should be unlocked, and a callback
which implements `onAuthenticationSucceeded` method. The `onAuthenticationSucceeded`
method triggers when a user is successfully authenticated by the system. Most of the
encountered biometric authentication implementations rely on this method being called,
without caring about the crypto object. Application logic responsible for unlocking
the application is usually included in this callback method. This approach is trivially
exploited by hooking into the application process and directly calling
`onAuthenticationSucceeded` method, as a result the application should be unlocked
without providing valid biometrics.

In order to implement biometric authentication in a secure manner, the Keystore key
which is inside of this crypto object has to be used for some application critical
cryptographic operation. That way even if a device become compromised and an attacker
makes a request, the Android Keystore would refuse to decrypt the data.
