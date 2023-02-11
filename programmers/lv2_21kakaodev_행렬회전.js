/**
맨 처음 판 만들고
cycle적용하면서 작은 수 기록

그냥 구현하면 될거같다.
**/

function firstStart(row, col){
    const arr = [];
    for(let i=0; i<row; i++) arr.push([]);
    
    let count=1;
    const arr2 = arr.map((val, idx)=>{
        for(let i=0; i<col; i++) val.push(count++);
        return val;
    })
    return arr2;
}

function cycle(arr, query){
    let [x1, y1, x2, y2] = query;
    [x1, y1, x2, y2] = [x1-1, y1-1, x2-1, y2-1];
    const row_leng = x2-x1;
    
    const part1 = arr[x1].slice(y1, y2);
    const part2 = [];
    for(let i=0; i<row_leng; i++){
        part2.push(arr[x1+i][y2]);
    };
    const part3 = arr[x2].slice(y1+1, y2+1);
    const part4 = [];
    for(let i=0; i<row_leng; i++){
        part4.push(arr[x1+1+i][y1]);
    };
    
    const all_parts = [...part1, ...part2, ...part3, ...part4];
    const min_val = Math.min(...all_parts);
    // console.log(part1, part2, part3, part4);
    //적용
    arr[x1].splice(y1+1, part1.length, ...part1);
    
    for(let i=0; i<row_leng; i++){
        arr[x1+1+i][y2] = part2[i];
    };

    arr[x2].splice(y1, part3.length, ...part3);
    
    for(let i=0; i<row_leng; i++){
        arr[x1+i][y1] = part4[i];
    };
    // console.log(arr);
    return [arr, min_val]; //n_arr, min_val
}

function solution(rows, columns, queries) {
    let arr = firstStart(rows, columns);
    let min_val = 0;
    const answer = [];
    queries.map((query, idx)=>{
        [arr, min_val] = cycle(arr, query);
        answer.push(min_val);
    })
    return answer;
}