import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Main {
    public static void main(String[] args) {
        int MAX_NUMBER = 1_234_000_100;
        long seed = System.currentTimeMillis();
        long max = seed + 5000;
        for (long i = seed; i <= max; i++) {
            Random random = new Random(i);
            int t1 = random.nextInt(MAX_NUMBER);
            int t2 = random.nextInt(MAX_NUMBER);
            int t3 = random.nextInt(MAX_NUMBER);
            int t4 = random.nextInt(MAX_NUMBER);
            System.out.println(t1);
            System.out.println(t2);
            System.out.println(t3);
            System.out.println(t4);
            System.out.println();
        }
    }
}
