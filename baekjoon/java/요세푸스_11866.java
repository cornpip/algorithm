import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

public class De {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("<");
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), k = Integer.parseInt(st.nextToken());
        Deque<Integer> q = new ArrayDeque<Integer>();
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }
        while (q.size() > 0) {
            int count = 0;
            while (k-1 > count) {
                q.add(q.poll());
                count++;
            }
            if(q.size() == 1) bw.write(String.valueOf(q.poll()).concat(">"));
            else bw.write(String.valueOf(q.poll()).concat(", "));
        }
        bw.close();
    }
}