public class t {
    
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class He {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        Stack<Integer> st = new Stack<Integer>();
        while (t > 0) {
            st.clear();
            String s = br.readLine();
            int flag = 1;
            for (int i = 0; i < s.length(); i++) {
//                System.out.printf("%d, %c\n", st.size(), s.charAt(i));
                if (s.charAt(i) == '(') st.push(1);
                else {
                    if (st.size() == 0) {
                        flag = 0;
                        break;
                    } else st.pop();
                }
            }
            if (st.size() != 0) flag = 0;

            if (flag == 1) System.out.println("YES");
            else System.out.println("NO");
            t--;
        }
    }
}