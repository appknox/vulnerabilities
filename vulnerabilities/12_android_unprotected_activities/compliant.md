
-   In this compliant solution the activity is not exported:

    <activity
        android:configChanges="keyboard|keyboardHidden|orientation"
        android:name=".media.yfrog.YfrogUploadDialog"
        android:theme="@style/ VulnerableTheme.Dialog"
        android:windowSoftInputMode="stateAlwaysHidden"
        android:exported="false">
    </activity>

    By declaring android:exported="false" for an activity tag in the
    AndroidManifest.xml file, the activity is restricted to only accept
    intents from within the same app or from an app with the same
    user ID.

-   This vulnerability was fixed in Twicca v0.9.31. Instead of declaring
    the activity exported="false" in AndroidManifest.xml, Twicca fixed
    this vulnerability by validating the caller of this activity. In
    the onCreate() method of the activity class, code was added to check
    if the package name of the caller is the same as the package name
    of itself. If the package names are different, the activity exits:

    public void onCreate(Bundle arg5) {
        super.onCreate(arg5);
        ...
        ComponentName v0 = this.getCallingActivity();
        if (v0 == null) {
            this.finish();
        } else if (!jp.r246.twicca.equals(v0.getPackageName())) {
            this.finish();
        } else {
            this.a = this.getIntent().getData();
            if (this.a == null) {
                this.finish();
            }
            ...
        }
    }

An Android developer can arbitrarily choose a package name, so
different app developers could choose the same package name.
Therefore, it is generally not recommended to use the package name
for validating the caller of the activity. The recommended
alternative is to check the developer's certificate, instead of the
package name.

However, considering the following facts, Twicca's solution may be
logical and safe against the exploit:

- Only one app with a particular package name can exist on
  Google Play.

- If a user tries to install an app whose package name already
  exists on the device, the installation either will fail or will
  overwrite the previously installed app.

