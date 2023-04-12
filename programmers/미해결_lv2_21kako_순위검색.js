/** 
2단 배열이면 sort안된다 생각하자.
index는 at으로 잡자
**/
function binarySearch(input, target, start, end){
    let mid = parseInt((start+end)/2);
    
    if ( mid == start || mid == end ) return mid;
    
    if ( input.at(mid) == target ) return mid;
    
    if ( input.at(mid) > target ) return binarySearch(input, target, start, mid);
    if ( input.at(mid) < target ) return binarySearch(input, target, mid, end);
}

function solution(info, query) {
    let infos = [];
    info.map((v)=>{
        let arr = v.split(" ");
        infos.push(arr);
    })
    infos.sort((a,b)=> +a.at(-1) - +b.at(-1));
    let infoScores = infos.map((v) => +v.at(-1));
    //console.log(infos);
    //console.log(infoScores);
    
    const answer = query.map((quy) => {
        quy = quy.split(" ");
        let [stack, a1, job, a2, career, a3, food, score] = quy;
        score *= 1;
        let idx = binarySearch(infoScores, score, 0, infoScores.length-1);
        //console.log(idx);
        //console.log(quy);
        let count = 0;
        //console.log(quy, idx);
        infos.slice(idx).forEach((v) => {
            let [i_stack, i_job, i_career, i_food, i_score] = v;
            i_score *= 1;
            if(i_score < score) return;
            if(stack !== "-" && stack !== i_stack) return;
            if(job !== "-" && job !== i_job) return;
            if(career !== "-" && career !== i_career) return;
            if(food !== "-" && food !== i_food) return;
            //console.log(v);
            count++;
        })
        return count;
    })
    return answer;
}