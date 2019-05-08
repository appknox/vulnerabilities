
あなたのアクティビティでの `FLAG_SECURE`の使用例を以下に挙げます。

   public class SecureActivity extends Activity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            // Set the Secure flag for this Window
            getWindow().setFlags(LayoutParams.FLAG_SECURE, LayoutParams.FLAG_SECURE);
        }
    }

