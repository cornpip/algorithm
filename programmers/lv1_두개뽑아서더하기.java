class Solution {
    public static Integer[] concat(Integer[] a, Integer[] b) {
//        System.out.printf("%s, %s\n",Arrays.toString(a), Arrays.toString(b));
        return Stream.of(a, b).flatMap(Arrays::stream).toArray(Integer[]::new);
    }

    public static Integer[][] combination(Integer[] numbers, int depth) {
        if (depth > numbers.length) return new Integer[][]{{}}; //불필요한 부분들 빨리 끝내고
        if (depth == 0) return new Integer[][]{{}};

        ArrayList<Integer[]> total_res = new ArrayList<Integer[]>();
        for (int i = 0; i < numbers.length; i++) {
            Integer[] n_numbers = Arrays.copyOfRange(numbers, i + 1, numbers.length);
            Integer[][] res = combination(n_numbers, depth - 1);
            for (Integer[] r : res) {
                if (r.length != depth - 1) continue; //빨리 끝난애들 거르기
                total_res.add(concat(new Integer[]{numbers[i]}, r));
            }
        }
        return total_res.toArray(new Integer[][]{{}});
    }
    
    public int[] solution(int[] numbers) {
        Integer[] r_numbers = Arrays.stream(numbers).boxed().toArray(Integer[]::new);
        
        HashSet<Integer> a = new HashSet<Integer>();   
        Integer[][] res = combination(r_numbers, 2);
        for(Integer[] re : res){
            Integer hap = 0;
            for(Integer r : re){
                hap += r;
            }
            a.add(hap);
        }
        int[] ans = a.stream().mapToInt(Integer::intValue).toArray();
        Arrays.sort(ans);
        return ans;
    }
}