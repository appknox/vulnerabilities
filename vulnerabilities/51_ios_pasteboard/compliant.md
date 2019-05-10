
Use application specific pasteboard. Also mark fields like passwords as
secure so that their data can never be copied

Pasteboards may be public or private. Public pasteboards are called
system pasteboards; private pasteboards are created by apps, and hence
are called app pasteboards. Pasteboards must have unique names.
UIPasteboard defines two system pasteboards, each with its own name and
purpose:

- `UIPasteboardNameGeneral` is for cut, copy, and paste operations
  involving a wide range of data types. You can obtain a singleton
  object representing the General pasteboard by invoking the
  generalPasteboard class method.
- `UIPasteboardNameFind` is for search operations. The string currently
  typed by the user in the search bar (`UISearchBar`) is written to this
  pasteboard, and thus can be shared between apps. You can obtain an
  object representing the Find pasteboard by calling the
  pasteboardWithName:create: class method, passing in
  UIPasteboardNameFind for the name.

Typically you use one of the system-defined pasteboards, but if
necessary you can create your own app pasteboard using
pasteboardWithName:create: If you invoke pasteboardWithUniqueName,
UIPasteboard gives you a uniquely-named app pasteboard. You can discover
the name of a pasteboard through its name property

Clear the Pasteboard once the application enters background. You can do
this by adding the following line in the method

`- (void)applicationDidEnterBackground:(UIApplication \*)` application in AppDelegate.

If you are using a custom Pasteboard, replace `[UIPasteboard generalPasteboard]` with your custom pasteboard.

    - (void)applicationDidEnterBackground:(UIApplication *)application
    {
        // Use this method to release shared resources, save user data, invalidate
        timers, and store enough application state information to restore your application
        to its current state in case it is terminated later.

        // If your application supports background execution, this method is called
        instead of applicationWillTerminate: when the user quits.

        [UIPasteboard generalPasteboard].items = nil;
    }

