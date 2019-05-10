
この非順守コード例は最後のセグメントを、 android.net.Uri.getLastPathSegment() を呼び出すことによって、ファイル名を示すことになっている paramUri パスから取り戻そうとしています。そのファイルは事前構成済みの親ディレクトリ IMAGE_DIRECTORY 内でアクセスされます。

    private static String IMAGE_DIRECTORY = localFile.getAbsolutePath();
    public ParcelFileDescriptor openFile(Uri paramUri, String paramString) throws FileNotFoundException {
        File file = new File(IMAGE_DIRECTORY, paramUri.getLastPathSegment());
        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    }

この規格に準拠していないコード例は、 `Uri.getLastPathSegment（）`を2回呼び出すことで、最初の非準拠のコード例を修正しようとしています。最初の呼び出しはURLデコードを意図しており、2番目の呼び出しは開発者が望む文字列を取得することです。

    private static String IMAGE_DIRECTORY = localFile.getAbsolutePath();
    public ParcelFileDescriptor openFile(Uri paramUri, String paramString) throws FileNotFoundException {
        File file = new File(IMAGE_DIRECTORY, Uri.parse(paramUri.getLastPathSegment()).getLastPathSegment());
        return ParcelFileDescriptor.open(file, ParcelFileDescriptor.MODE_READ_ONLY);
    }

