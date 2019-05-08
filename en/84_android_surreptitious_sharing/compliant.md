
We provided a fix for app developers that checks with _fstat_ if a file is
owned by the receiving app only and then prevents the opening of it.
Due to the requirement of using _fstat_ our Java fix was only available for
Android >= 5. We strongly recommend to use this library to fix the
issue in your app:

[https://github.com/appknox/SafeContentResolver](https://goo.gl/Gsz1bh).
