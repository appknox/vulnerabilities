
Android SDK offers a way for developers to present a
[`Preferences activity`](https://developer.android.com/reference/android/preference/PreferenceActivity.html).
to users, allowing them to extend this abstract class and adapt it to their needs.

This abstract class will parse the extra data fields received on a Intent,
in particular the
`PreferenceActivity.EXTRA_SHOW_FRAGMENT(:android:show_fragment)` and
`PreferenceActivity.EXTRA_SHOW_FRAGMENT_ARGUMENTS(:android:show_fragment_arguments)`

It is expected that the first field contains the `Fragment`
class name and the second one contains the input bundle passed
to the `Fragment`.

Due to the fact that the `PreferenceActivity` uses reflection to
load the fragment, this can lead to load an arbitrary class inside the
package or the Android SDK. The loaded class runs in the context of the
application that exports this activity.

