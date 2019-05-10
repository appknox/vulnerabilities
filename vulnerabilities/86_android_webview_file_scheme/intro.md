
The WebView class displays web pages as part of an activity layout.
The behavior of a WebView  object can be customized using the WebSettings
object, which can be obtained from WebView.getSettings().

Major security concerns for WebView are about the
`setJavaScriptEnabled()`, `setPluginState()`,
and `setAllowFileAccess()` methods.

When an activity has WebView embedded to display web pages, any application
can create and send an Intent object with a given URI to the activity to
request that a web page be displayed.

WebView can recognize a variety of schemes, including the `file:scheme`.
A malicious application may create and store a crafted content on its
local storage area, make it accessible with MODE_WORLD_READABLE permission,
and send the URI (using the `file:scheme`) of this content to a target activity.
