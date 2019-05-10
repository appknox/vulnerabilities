
If you are using a Service for sharing data between only your own apps,
it is preferable to use the `android:protectionLevel` attribute set to
`signature` protection. Signature permissions do not require user
confirmation, so they provide a better user experience and more
controlled access to the Service when the apps accessing the data are
signed with the same key
