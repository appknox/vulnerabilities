
This activity receives `android.intent.action.SEND` or
`android.intent.action.SEND_MULTIPLE` intents and accepts a file-scheme as data
URI `(file://...)` as parameter. It may be vulnerable to surreptitious sharing:
a malicious application may set a URI referencing a private file of this
application, and if no proper sanity checking is done this might be used
to obtain the referenced file.

