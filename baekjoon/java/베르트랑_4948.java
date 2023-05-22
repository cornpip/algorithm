import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Prime {
    public static int[] prime = new int[246914];

    public static boolean getPrime(double num) {
        int memory = prime[(int) num];
        if (memory == -1) return false;
        if (memory == 1) return true;

        double num_sqrt = Math.floor(Math.sqrt(num));
        for (double i = 2; i <= num_sqrt; i++) {
            if (num % i == 0) {
                prime[(int) num] = -1;
                return false;
            }
        }
        prime[(int) num] = 1;
        return true;
    }

    public static void main(String[] args) throws IOException {
//        System.out.println(Arrays.toString(prime));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        while (n != 0) {
            int count = 0;
            for (double i = n + 1; i <= 2 * n; i++) {
                if (getPrime(i)) count++;
            }
//            System.out.println(count);
            sb.append(count).append("\n");
            n = Integer.parseInt(br.readLine());
        }
        System.out.print(sb);
    }
}