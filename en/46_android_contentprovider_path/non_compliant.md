
This non-compliant code example tries to retrieve the last segment from
the path paramUri, which is supposed to denote a file name, by calling
`android.net.Uri.getLastPathSegment()`. The file is accessed in the
pre-configured parent directory IMAGE\_DIRECTORY.

    private static String IMAGE_DIRECTORY = localFile.getAbsolutePath();
    public ParcelFileDescriptor openFile(Uri paramUri, String paramString) throws FileNotFoundException {
        File file = new File(IMAGE_DIRECTORY, paramUri.getLastPathSegment());
        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    }

This non-compliant code example attempts to fix the first non-compliant
code example by calling `Uri.getLastPathSegment()` twice. The first call
is intended for URL decoding and the second call is to obtain the string
the developer wanted.

    private static String IMAGE_DIRECTORY = localFile.getAbsolutePath();
    public ParcelFileDescriptor openFile(Uri paramUri, String paramString) throws FileNotFoundException {
        File file = new File(IMAGE_DIRECTORY, Uri.parse(paramUri.getLastPathSegment()).getLastPathSegment());
        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    }

