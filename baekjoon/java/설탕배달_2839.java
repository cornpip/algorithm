import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Hello {
    public static double over = 1e9;

    public static double dp(double[] dp_list, int i) {
        if (i <= 2) return over;
        if (dp_list[i] != 0) return dp_list[i];

        dp_list[i] = Math.min(dp(dp_list, i - 3), dp(dp_list, i - 5)) + 1;
        return dp_list[i];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int i = Integer.parseInt(br.readLine());

        double[] dp_list = new double[i + 1];
        dp_list[3] = 1;
        if (i >= 5) dp_list[5] = 1;
        double res = dp(dp_list, i);

        if (res >= over) System.out.println(-1);
        else System.out.println((int) res);
    }
}