function solution(n, info) {
    let answer = [-1];
    let memorize_diff = 0;

    function calcular(target){
        let [lion, peach] = [0, 0];
        info.forEach((val, idx)=>{
            if(target[idx] > val) lion += (10-idx);
            else{
                if(val > 0) peach += (10-idx);  
            }
        })
        // diff from peach
        return lion-peach;
    }

    //idx는 뒤에서 부터 올거고요
    function dfs(remain_arrow, ing_target, idx){
        if(remain_arrow === 0){
            const diff = calcular(ing_target);
            if(diff > memorize_diff) {
                answer = ing_target;
                memorize_diff = diff;
            }else if(diff !== 0 && diff === memorize_diff){
                if (ing_target[10] > answer[10]) answer = ing_target;
            }
            return;
        }

        for(let i=idx; i>=0; i--){
            const peach_i_arrow = info[i];
            const c_ing_target = [...ing_target];
            if( remain_arrow > peach_i_arrow ){
                c_ing_target[i] = peach_i_arrow + 1;
                dfs(remain_arrow-(peach_i_arrow+1), c_ing_target, i-1);
            }else{
                c_ing_target[10] += remain_arrow;
                dfs(0, c_ing_target, i-1);
            }
        }

        //남은 걸 마지막에 다 주면 dfs순으로 return조건을 만족한다를 확신 못하는거 아닌가
        const c_ing_target = [...ing_target];
        c_ing_target[10] += remain_arrow;
        dfs(0, c_ing_target, -1);
        return;
    }

    dfs(n, new Array(11).fill(0), 10);
    return answer; //ans는 최종 과녁에 맞춘 배열
}