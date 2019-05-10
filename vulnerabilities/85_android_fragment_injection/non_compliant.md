
- Determine the minSDKVersion and maxSDKVersion to determine what will be the behaviour of the class.
- Find exported Activities that extends the `PreferenceActivity` class.

The following example shows a Activity that extends this activity :

    public class MyPreferences extends PreferenceActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

