
The following entry in the AndroidManifest.xml file makes the content
provider private so that other apps cannot access the data:

    <provider
        android:name=".content.AccountProvider"
        android:exported="false"
        android:authorities="jp.co.vulnerable.accountprovider" />

