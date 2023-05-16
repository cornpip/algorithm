class Solution {
    public int go(int start, int num, int total){
        while(true){
            int sum = 0;
            for(int i=0; i<num; i++) {
                sum += start + i;
            }
            if(sum == total) break;
            start++;
        }
        return start;
    }

    public int[] solution(int num, int total) {
        int guess = total / num;
        int lower = (int)Math.ceil((num-1)/2);
        int res = go(guess-lower, num, total);
        int[] ans = new int[num];
        for(int i=0; i< num; i++){
            ans[i] = res;
            res++;
        }
        return ans;
    }
}
