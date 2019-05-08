
Many email and messaging apps on Android utilize the Intent API for sending
files shared from other apps such as Android’s gallery. These Intents are
standardized for sending and receiving content. Instead of sending entire
files, such as videos, via this API, only URIs are exchanged pointing to the
actual storage position. A vulnerability in this Intent API, which is
present in many published communication apps allowing privilege escalation
and data leakage.

The main issue lies in the fact that apps cannot only access their private data
directories using `Context.openFileOutput(String name, int mode)`, but also
using _file_ URIs. While these URIs are normally used to access files on the
SD card, via `file:///sdcard/paper.pdf` for example, they can also point to
private files, e.g., `file:///data/data/com.example.app/files/paper.pdf`.
If an app registers Intent Filters to support Android’s sharing API or defines
custom Intents accepting URIs, they are potentially accepting _file_ URIs that
could also point to their own private files. For apps facilitating
communication, like email or messaging apps, this leads to what we call
_Surreptitious Sharing_. Investigating the AOSP source code reveals that
support for _file_ URIs using `Context.openFileOutput(String name, int mode)`
(similar checks are present in `openAssetFileDescriptor`) was planned to be
removed (see inline comments in `openInputStream` method in
[ContentResolver]
(https://goo.gl/Qyx84j)).


