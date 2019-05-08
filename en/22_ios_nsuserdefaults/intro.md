
NSUserDefaults are stored in plist in binary format, with no encryption,
and is stored in your app's directory. Any user can edit, see, share,
move and whatever they want to. Thus, if any sensitive information is
stored in NSUserDefaults then it may reach wrong hands & can be used for
personal use later on.
