function solution(id_list, report, k) {
    const answer = [];
    const id_object = {}
    id_list.forEach((val)=>{
        id_object[val] = new Set();
    })
    
    report.forEach((val)=>{
        const [start, end] = val.split(' ');
        id_object[end].add(start)
    })
    
    const id_count = {}
    id_list.forEach((val)=>{
        id_count[val] = 0;
    })
    for (const [key, val] of Object.entries(id_object)){
        if (val.size >= k){
            for(const i of val) id_count[i]++;
        }
    }
    for (const val of Object.values(id_count)) answer.push(val);
    return answer;
}