import java.io.*;
import java.util.Collections;
import java.util.PriorityQueue;

public class Hip {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());

        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        int temp = 0;
        while(t > 0){
            temp = Integer.parseInt(br.readLine());
            if(temp == 0){
                if(q.size() == 0) bw.write("0");
                else bw.write(String.valueOf(q.poll()));

                if(t > 1) bw.newLine();
            }else{
                q.add(temp);
            }
            t--;
        }
        bw.close();
    }
}