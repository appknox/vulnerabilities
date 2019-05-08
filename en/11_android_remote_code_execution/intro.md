
For API level JELLY\_BEAN or below, allowing an app to use the
addJavascriptInterface method with untrusted content in a WebView leaves
the app vulnerable to scripting attacks using reflection to access
public methods from JavaScript. Untrusted content examples include
content from any HTTP URL (as opposed to HTTPS) and user-provided
content. The method `addJavascriptInterface(Object, String)` is called
from the `android.webkit.WebView` class. Sensitive data and app control
should not be exposed to scripting attacks.
