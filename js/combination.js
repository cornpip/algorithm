function combination(in_arr, count){
    if(count===1) return in_arr.map((val)=>[val]);

    const res = [];
    in_arr.forEach((val, idx, arr)=>{
        const rest = in_arr.slice(idx+1);
        const _res = combination(rest, count-1);
        _res.forEach((val2, idx2)=>{
            res.push([val, ...val2]);
        })
    })
    return res;
}

const see = combination([1,2,5,6], 4);
console.log(see);