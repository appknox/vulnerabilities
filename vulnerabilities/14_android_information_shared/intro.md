
In Android apps, data can be communicated via intents, or data can be
written to files, distributed using shared references, or stored in
databases. In all these cases, if the data is sensitive, it is important
to keep the data secure. That is, it should not be possible for other
apps (or, more strictly, apps with different userids) to be able to
access this data, or for the data to be accessible to other programs or
people, if the data owner does not intend that.

Data security (for non-intent communication channels) can be supported
by creating the file, shared preference or database with MODE\_PRIVATE
on internal storage or with MODE\_PRIVATE and encrypted (using secure
encryption techniques, and using an encryption key only secure
parties/apps have) on external storage. MODE\_PRIVATE is a constant
defined by the class android.content.Context. It may be used as the mode
parameter in the methods openFileOutput(), getSharedPreferences(),
andopenOrCreateDatabase() (which are all also defined in the class
android.content.Context).

Static taint flow analysis can be done for a set of apps, to trace data
from each source (an input of data which cannot be fully predicted by
static analysis, e.g., text input by a user) to reachable sinks (data
output to a location that other applications or methods can access,
e.g., sending the data over a Bluetooth connection). Taint flow analysis
helps users understand many possible source to sink flows, including
flows that include intents and/or static fields.
