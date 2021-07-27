
The LAContext helper class is used for local authentication, it does not verify
anything externally but relies on the iOS to present the relevant dialog and confirm
authentication. Once a new LAContext instance is set up, the `evaluatePolicy` method is
called, giving iOS a chance to present the relevant dialog and perform the
authentication. Depending on the success or failure of the authentication itself, a
`reply` block is invoked that includes a boolean indicating if it was successful or not.
This response can be bypassed as we can intercept the operating systems response to
the application and set the response as true, and original intended code block is
executed, just like it would have under normal conditions.

In order to implement biometric authentication in a secure manner, the keychain items
should be protected with access control flags such as `kSecAccessControlBiometryAny`
then a valid set of biometrics (either TouchID or FaceID) must be presented before the
key is released from the Secure Enclave to decrypt the keychain entry itself.
