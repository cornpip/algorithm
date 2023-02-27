/**
 * 
 * @param {*} in_arr 
 * @param {*} depth: n>=1 (arr에서 n개 뽑을게) 
 * @returns 
 */

function permutation(in_arr, count){
    if (count === 1) return in_arr.map((val)=>[val]);

    const res = [];
    in_arr.forEach((val, idx, arr)=>{
        const rest = [...in_arr.slice(0,idx), ...in_arr.slice(idx+1)];
        const _res = permutation(rest, count-1);
        _res.forEach((val2, idx2)=>{
            res.push([val, ...val2]);
        })
    })
    return res;
}

const see = permutation([1,4,5,2], 4);
console.log(see);