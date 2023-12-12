
    public class Noncompliant extends AppCompatActivity {
        @Override
        protected void onCreate(Bundle savedInstanceState) {
            Intent intent = getIntent();
            Intent forward = (Intent) intent.getParcelableExtra("anotherintent");
            startActivity(forward);
        }
    }
