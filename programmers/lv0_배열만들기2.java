import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


class lv0_배열만들기2{
    public void main(String[] args){
        Solution s = new Solution();
        int[] res = s.solution(5, 555);
        System.out.println(Arrays.toString(res));
    }
}

class Solution {
    private boolean check(String a) {
//        System.out.println(a);
        for (int i = 0; i < a.length(); i++) {
            char aa = a.charAt(i);
            if (aa != '0' && aa != '5') return false;
        }
        return true;
    }

    public int[] solution(int l, int r) {
        List<Integer> ans = new ArrayList<>();
        for (int i = l; i <= r; i++) {
            String tem = i + "";
            if (check(tem)) ans.add(i);
        }

        if (ans.size() == 0) return new int[]{-1};

        int[] res = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            res[i] = ans.get(i);
        }
        return res;
    }
}