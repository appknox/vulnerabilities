
        import java.security.SecureRandom;

        public class generateRandom {
            public static void main(String args[]) {
                SecureRandom rand = new SecureRandom();
                int rand_int = rand.nextInt(1000);
            }
        }
           