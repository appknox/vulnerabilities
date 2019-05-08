
-  minSDKVersionとmaxSDKVersionを決定し、クラスの動作を決定します。
-  `PreferenceActivity`クラスを拡張した、エクスポートされたアクティビティを検索します。

次の例は、このアクティビティを拡張するアクティビティを示しています。

    public class MyPreferences extends PreferenceActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

