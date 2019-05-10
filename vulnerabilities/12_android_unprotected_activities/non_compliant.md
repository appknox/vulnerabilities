
This non-compliant code example shows an `AndroidManifest.xml` file for an
application that exports the activity to other apps, but does not
restrict access to its sensitive activity:

    <activity
        android:configChanges="keyboard|keyboardHidden|orientation"
        android:name=".media.yfrog.YfrogUploadDialog"
        android:theme="@style/Vulnerable.Dialog"
        android:windowSoftInputMode="stateAlwaysHidden">
        <intent-filter android:icon="@drawable/yfrog_icon" android:label="@string/YFROG">
            <action android:name="jp.co.vulnerable.ACTION_UPLOAD" />
            <category android:name="android.intent.category.DEFAULT" />
            <data android:mimeType="image/*" />
            <data android:mimeType="video/*" />
        </intent-filter>
    </activity>

`android:name` refers to the name of the class that implements this
activity. The name of the package is `jp.co.vulnerable` so the fully
qualified name of the class implementing this activity is
`jp.co.vulnerable.media.yfrog.YfrogUploadDialog`. Since the intent filter
is defined, this activity is exported to other apps.
