import java.io.*;
import java.util.Stack;

public class Sequence {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder stb = new StringBuilder();
        int t = Integer.parseInt(br.readLine());

        Stack<Integer> st = new Stack<Integer>();
        st.push(1); stb.append("+\n");

        int number = 0, value = 1;
        while (t > 0) {
            number = Integer.parseInt(br.readLine());
            while (number > value) {
                value++;
                st.push(value); stb.append("+\n");
            }
            int top = st.pop();
            if( top != number ){
                stb.delete(0, stb.length());
                stb.append("NO");
                break;
            }else{
                if(t == 1) stb.append("-");
                else stb.append("-\n");
            }
            t--;
        }
        System.out.println(stb.toString());
    }
}