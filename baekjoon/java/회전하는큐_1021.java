import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Bang {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        String[] a = br.readLine().split(" +");
        Queue<Integer> q = new LinkedList<>();
        for (int i = 1; i <= n; i++) {
            q.offer(i);
        }
        int total_count = 0, len = n;

        for (String aa : a) {
            int head = q.peek(), count = 0;
            while (!Integer.valueOf(aa).equals(head)) {
                q.offer(q.poll()); count++;
                head = q.peek();
            }
            total_count += Math.min(count, len-count);
            q.poll(); len--;
        }
        System.out.println(total_count);
    }
}