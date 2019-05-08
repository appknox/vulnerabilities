
Android allows the attribute `android:debuggable` to be set to true so
that the app can be debugged. By default this attribute is disabled,
i.e., it is set to false, but it may be set to true to help with
debugging during development of the app. However, an app should never be
released with this attribute set to true as it enables users to gain
access to details of the app that should be kept secure. With the
attribute set to true, users can debug the app even without access to
its source code.
