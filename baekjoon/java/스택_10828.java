import java.io.*;
import java.util.*;

public class Main2 {
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void write(String s) throws IOException {
        bw.write(s);
        bw.newLine();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        LinkedList<Integer> list = new LinkedList<>();

        while (t > 0) {
            String[] cmd = br.readLine().split(" +");
            if (cmd[0].equals("push")) list.addFirst(Integer.parseInt(cmd[1]));
            if (cmd[0].equals("pop")) {
                if (list.isEmpty()) write("-1");
                else write(String.valueOf(list.pollFirst()));
            }
            if (cmd[0].equals("size")) write(String.valueOf(list.size()));
            if (cmd[0].equals("empty")) {
                if (list.isEmpty()) write("1");
                else write("0");
            }
            if (cmd[0].equals("top")) {
                if (list.isEmpty()) write("-1");
                else write(String.valueOf(list.getFirst()));
            }
            t--;
        }
        bw.flush();
        bw.close();
    }
}
