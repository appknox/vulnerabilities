
        import java.util.Random;

        public class generateRandom {
            public static void main(String args[]) {
                Random rand = new Random();
                int rand_int = rand.nextInt(1000);
            }
        }

        
OR


        import java.lang.Math;

        public class generateRandom {
            public static void main(String[] args) {
                double randomValue = Math.random();
            }
        }
           