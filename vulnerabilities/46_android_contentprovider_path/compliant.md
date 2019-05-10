
By using the canonicalized path, directory traversal will be mitigated
even when a doubly-encoded path is supplied.

    private static String IMAGE_DIRECTORY = localFile.getAbsolutePath();
    public ParcelFileDescriptor openFile(Uri paramUri, String paramString) throws FileNotFoundException {
        String decodedUriString = Uri.decode(paramUri.toString());
        File file = new File(IMAGE_DIRECTORY, Uri.parse(decodedUriString).getLastPathSegment());
        if (file.getCanonicalPath().indexOf(localFile.getCanonicalPath()) != 0) {
            throw new IllegalArgumentException();
        }
        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    }

For example, the following double encoded string will circumvent the fix.

    %252E%252E%252F%252E%252E%252F%252E%252E%252Fdata%252Fdata%252Fcom.example.android.app%252Fshared_prefs%252FExample.xml

The first call of `Uri.getLastPathSegment()` will decode "%25" to "%"
and return the string:

    %2E%2E%2F%2E%2E%2F%2E%2E%2Fdata%2Fdata%2Fcom.example.android.app%2Fshared_prefs%2FExample.xml

When this string is passed to the second `Uri.getLastPathSegment()`, "%2E"
and "%2F" will be decoded and the result will be:

    ../../../data/data/com.example.android.app/shared_prefs/Example.xml

