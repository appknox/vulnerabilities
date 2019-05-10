
If you are using a Content Provider for sharing data between only your
own apps, it is preferable to use the `android:protectionLevel` attribute
set to "signature" protection. Signature permissions do not require user
confirmation, so they provide a better user experience and more
controlled access to the content provider data when the apps accessing
the data are signed with the same key

If the Content Provider is called within itself, then don't export it or
use Intent-Filter for custom permissions
