function lowest(lottos, win_nums){
    const a = new Set(win_nums);
    let [count, zeros] = [0,0];
    lottos.forEach((val)=>{
        if(val !== 0){
            if(a.has(val)) count++;
        }else{
            zeros++;
        }
    })
    return [count, zeros];
}

const res = {6:1, 5:2, 4:3, 3:4, 2:5};
function solution(lottos, win_nums) {
    const [count, zeros] = lowest(lottos, win_nums);
    
    const low = res[count] === undefined ? 6 : res[count];
    const high = res[count+zeros] === undefined ? 6 : res[count+zeros];
    const answer = [];
    answer.push(high, low);
    return answer;
}