/***
fucn1 10진수 k진수로
func2 소수인가 (0이 들었는가 판단 필요X)

0을 기점으로 조건 체크
전index~현index 까지 확인(전전index ~ 전index 까지는 확인필요X)

기존에 찾은 0 index가 없다면 P0 확인
있다면 0P0
마지막 0index 이후에 index가 더 큰상태로 끝났다면 0P 확인
0index가 없이 index가 큰 상태로 끝났다면 P확인
0이 한번도 안나오고 끝났을 때 P확인
***/

function toK(n, k){
    const k_arr = [];
    while(n>=k){
        const remain = n%k;
        n = parseInt(n/k);
        k_arr.push(remain);
        if(n<k)k_arr.push(n);
    };
    k_arr.reverse();
    // console.log(k_arr);
    return k_arr;
}

function primeNumber(n){
    if(n===1) return false;
    const count = parseInt(Math.sqrt(n));
    for(let i=2; i<=count; i++){
        if(n%i === 0) return false;   
    };
    return true;
}

function solution(n, k) {
    let total_count = 0;
    
    const k_arr = toK(n, k);
    const leng = k_arr.length;
    let zero_idx = 0; //시작이 0일 순 없으니까 무관
    for(let [idx, val] of k_arr.entries()){
        let cut_arr = [];
        if(val===0 && zero_idx===0){ //맨앞이 0일 경우는 없다.
            cut_arr = k_arr.slice(0, idx);
            zero_idx = idx;
        }else if(val===0 && zero_idx!==0){
            cut_arr = k_arr.slice(zero_idx+1, idx);
            zero_idx = idx;
        }else if(idx === leng-1 && val !== 0 && zero_idx !== 0){
            cut_arr = k_arr.slice(zero_idx+1);
        }else if(idx === leng-1 && zero_idx === 0){
            cut_arr = k_arr;
        }
        if(cut_arr.length !== 0){
            let p = parseInt(cut_arr.join(""));
            if(primeNumber(p)) {
                total_count++;
                // console.log(p);
            }
        }
    }
    return total_count;
}