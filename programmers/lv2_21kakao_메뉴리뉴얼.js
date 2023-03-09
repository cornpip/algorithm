/**
 * js에서 조합은?
 * 하나에서 조합을 써서 비교못함
 * 그 곳에 없는 알파벳이 있을 수 있으니까
 * 모든 알파벳을 취합하고 거기서 조합을 하자.
 * 
 * 최악의 경우 
 * 알파벳 26개
 * 26C10, 26C9, 26C8, ... , 26C2  ( 26C10은 500만 )
 * 
 * 500만에서 실행횟수는 덧셈으로 가는거라 생각했는데
 * 이렇게 보니까 500만개를 20개와 대조해봐야되는데 맞는게 없다면 끝까지 대조해보는거고
 * 대조 로직과 별개로 500만 * 20이야 (최악의 경우로 보면 length가 짧은 애들이 없는거다)
 * 
 * 조합 분할하면 충분한 최악에도 10(course)*20(orders)*1000( 10C5가 600쯤 )*19(대조)
 * 
 * 마지막에 정렬까지 잊지말기, 구성 개수 같은 상태에서 빈도 수 가장 많거나 같은것만 후보에 오름
 * 메뉴 안붙어 있어도 된다.
 * 
 * 아 너무 comb를 하나의 세트메뉴로 생각했다.
 * 검색할 때는 단일 메뉴로 따서 검색해서 확인해야하고 그렇게하면
 * 같은 조합에 배열만 다른것들이 나오므로 그거까지 처리필요
 * => 지금 문자"열"에 의미는 없다. 처음 order를 정렬하자.
**/

function solution(orders, course) {
    function combination(order, count) {
        // combination(order: string, count: number): Array<string>
        if (count > order.length) return [];
        if (count === 1) return order.split("");

        const res = [];
        for (let [idx, val] of Object.entries(order)) {
            const rest = order.slice(Number(idx) + 1); //아 Object.entries()는 key value를 string으로 반환한다.
            const _res = combination(rest, count - 1);
            _res.map((_res_val) => {
                res.push(val + _res_val);
            })
        }
        return res;
    }

    function comb_check(order, comb) {
        // comb_check(order: string, comb: string): boolean
        if (comb.length > order.length) return false; // comb가 더 길면 pass
        for(let v of comb){
            const regex = new RegExp(`${v}`, `g`);
            if(!regex.test(order)) return false;
        };
        return true;
    }

    const visited = new Set();
    const leng_orders = orders.length;
    const result = [];
    orders = orders.map((v)=> v.split("").sort().join(""));

    course.map((count) => {
        let [res, res_comb] = [0, []];
        orders.map((order, idx2) => {
            const all_comb = combination(order, count);

            all_comb.map((comb) => {
                if (visited.has(comb)) return; //이미 조회한 조합은 pass
                visited.add(comb);

                // 빠른 탈출위해 for문으로 
                let _res = 1; //추출된 order
                for (let i = 0; i < leng_orders; i++) {
                    if (idx2 === i) continue; //조합 추출한 order은 pass
                    if (comb_check(orders[i], comb)) _res += 1;
                };

                if (_res < 2){
                    return;
                }else if (_res > res){
                    res = _res;
                    res_comb = [comb];
                }else if ( _res === res){
                    res_comb.push(comb);
                }
            })
        });
        result.push(...res_comb);
    })
    result.sort();
    return result;
}