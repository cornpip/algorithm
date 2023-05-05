class Solution {
    public int solution(int[] common) {
        int[] res = check(common);
        // System.out.printf(Arrays.toString(res));
        if(res[0] == 1) {
            // System.out.printf("%d, %d", common[common.length-1], res[1]);
            return common[common.length-1] + res[1];
        }else return common[common.length-1] * res[1];
    }
    
    private int[] check(int[] common){
        int count = 0;
        int d = common[1] - common[0];
        
        for(int i=0; i<common.length-1; i++){
            if (count == 10) break;
            if (d == common[i+1] - common[i]){
                count++;
                d = common[i+1] - common[i];
                continue;
            } else {
                if (common[0] == 0) return new int[]{0, 0};
                return new int[]{0, common[1]/common[0]};   
            }
        }
        return new int[]{1, d};
    }
}