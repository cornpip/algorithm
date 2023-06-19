public class combination_list {
    static List<List<Integer>> combination(List<Integer> list, List<Integer> result, int depth) {
        List<List<Integer>> r = new ArrayList<>();
        if (result.size() == depth) {
            r.add(result);
            return r;
        }
        for (int i = 0; i < list.size(); i++) {
            List<Integer> n_list = new ArrayList<>(list.stream().skip(i + 1).collect(Collectors.toList()));
            List<Integer> n_result = new ArrayList<>(result.stream().collect(Collectors.toList()));
            n_result.add(list.get(i));
            List<List<Integer>> rr = combination(n_list, n_result, depth);
            for (List<Integer> rrr : rr) {
                r.add(rrr);
            }
        }
        return r;
    }
}