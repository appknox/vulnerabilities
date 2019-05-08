
On Android, declaring an intent filter for an activity in the
`AndroidManifest.xml` file means that the activity may be exported to
other apps. If the activity is intended solely for the internal use of
the app and an intent filter is declared, then any other apps, including
malware, can activate the activity for unintended use.

In the case of the vulnerability in the Twicca app (in versions 0.7.0
through 0.9.30), by launching Twicca's activity, another app that does
not have permission to access the SD card or network could upload images
or movies stored on the SD card to a social networking service with the
Twicca user's Twitter account.
