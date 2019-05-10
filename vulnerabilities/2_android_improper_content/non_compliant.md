
MovatwiTouch, a Twitter client application, used a content provider to
manage Twitter's consumer key, consumer secret, and access token.
However, the content provider was made public, which enabled
applications installed on users' devices to access this sensitive
information.

The following entry in the AndroidManifest.xml does not have the
`android:exported` attribute, which means, before API Level 16, the
content provider is made public:

    <provider
        android:name=".content.AccountProvider"
        android:authorities="jp.co.vulnerable.accountprovider" />

