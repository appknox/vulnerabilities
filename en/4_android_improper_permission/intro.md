
If an app is using a granted permission to respond to a calling app then
it must check that the calling app as that permission as well.
Otherwise, the responding app may be granting privileges to the calling
app that it should not have. (This is sometimes called the "confused
deputy" problem.)

The methods `Context.checkCallingPermission()` and
`Context.enforceCallingPermission()` can be used to ensure that the
calling app has the correct permissions.
