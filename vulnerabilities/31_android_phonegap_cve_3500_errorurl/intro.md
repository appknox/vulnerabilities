
Cordova-based applications make use of a WebView in order to interact
with the user. This vulnerability uses the errorurl parameter which can
be passed via Intent extras (in CordovaActivity) by a malicious caller,
but it is not automatically loaded into a WebView on application load.
The errorurl will only be rendered by the WebView when a network request
fails. This presents a vulnerability which can be exploited whereby a
malicious caller could launch the Activity.
