//재미로 추상화 붙여볼까?
function combination(total, count) {
    if (Array.isArray(total)) {
        return array_combination(total, count);
    }else if(typeof(total) === "number"){
        return number_combination(total, count);
    }

    function array_combination(total, count) {
        if (count === 1) return total.map((val) => [val]);

        const res = [];
        total.forEach((val, idx, arr) => {
            const rest = total.slice(idx + 1);
            const _res = array_combination(rest, count - 1);
            _res.forEach((val2, idx2) => {
                res.push([val, ...val2]);
            })
        })
        return res;
    }

    function number_combination(total, count){
        if (count > total) return 0;
        if (count === 1) return total;

        const loop_arr = new Array(total).fill(1);
        let res = 0;
        loop_arr.forEach((val, idx)=>{
            const rest = total-(idx+1);
            const _res = number_combination(rest, count-1);
            res += _res;
        })
        return res;
    }
}

// const res = combination([1, 2, 5, 6], 2);
// const res = combination(10, 5);

let res = 0;
for(let i=1; i<=10; i++){
    res += combination(10, i);
}
console.log(res);