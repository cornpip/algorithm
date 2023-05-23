import java.io.*;

public class Cycle {
    public static int[] get_num(int num){
        int left = (int) Math.floor(num/10);
        int right = num % 10;
        return new int[]{left,right};
    }

    public static int cycle(int left, int right) {
        int[] l_r = get_num(left+right);
        String res = String.valueOf(right) + l_r[1];
        return Integer.valueOf(res);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int res = 0, count = 1;
        int[] l_r = get_num(n);

        while(true){
            res = cycle(l_r[0], l_r[1]);
            if(res == n) break;
            count++;
            l_r = get_num(res);
        }
        System.out.println(count);
    }
}