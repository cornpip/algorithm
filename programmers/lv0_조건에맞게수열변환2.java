import java.util.*;

class Solution {
    public int[] get_arr(int[] arr, int count) {
        int[] n_arr = Arrays.copyOf(arr, arr.length);
        while (count > 0) {
            int idx = 0;
            for(int val: n_arr){
                if( val >= 50 && val%2 == 0 ) n_arr[idx] = val/2;
                else if( val < 50 && val%2 == 1) n_arr[idx] = val*2 + 1;
                else n_arr[idx] = val;
                idx++;
            }
            count--;
        }
        return n_arr;
    }

    public int solution(int[] arr) {
        int ans = 0;
        int[] pre_tmp = get_arr(arr, ans);
        while(true){
            int[] tmp = get_arr(arr, ans+1);
            if( Arrays.equals(pre_tmp, tmp) ) break;
            pre_tmp = tmp;
            ans++;
        }

        return ans;
    }
}