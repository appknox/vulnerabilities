
    public class MainActivity extends AppCompatActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);

            Intent intent = getIntent();
            Intent forward = (Intent) intent.getParcelableExtra("anotherintent");

            ComponentName name = forward.resolveActivity(getPackageManager());
            if (name.getPackageName().equals("safePackage") &&
                    name.getClassName().equals("safeClass")) {
                startActivity(forward);
            }
        }
    }
