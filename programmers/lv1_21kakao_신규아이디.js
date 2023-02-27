/**
    처음과 끝의 점 제거, 연속 점 하나로 치환
    처음 끝 점 삭제
    비었으면 a
    3글자이상 15글자이하
**/

function solution(new_id) {
    new_id = new_id.toLowerCase();
    const reg1 = /[a-z0-9-_.]/g;
    const reg2 = /\.{2,}/g;
    let res = new_id.match(reg1).join("");
    res = res.replace(reg2, ".");
    if (res === "." | !res) res = "a"
    
    if (res[0] === ".") res = res.slice(1);
    if (res.at(-1) === ".") res = res.slice(0, res.length-1);
    
    while(res.length < 3){
        res += res.at(-1);   
    }
    
    if(res.length > 15){
        res = res.slice(0, 15);
        if (res.at(-1) === ".") res = res.slice(0, res.length-1);
    }
    
    return res;
}