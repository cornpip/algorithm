/**
 * 구현문제고 몇몇 테케 통과못하는 상태
 * 알고리즘에 따른 값이 틀린값인 듯 한데....
 */

function calcular_fee(fees, manage_time, sort_car_num){
    const res = [];
    const [base_minute, base_fee, extra_unit, extra_fee] = fees;
    sort_car_num.forEach((val)=>{
        let s_val = String(val).padStart(4, '0');
        const minute = manage_time.get(s_val);
        if (minute <= base_minute) {
            res.push(base_fee);
        }else{
            let charge = base_fee + parseInt((minute-base_minute)/extra_unit) * extra_fee;
            if((minute-base_minute)%extra_unit !== 0) charge += extra_fee;
            // if(typeof(charge) !== "number") throw new Error("~~~");
            // if( !Number.isInteger(charge) ) throw new Error("~~~");
            res.push(charge);
        }
    });
    // if(sort_car_num.length !== res.length) throw new Error("~~~");
    return res;
}

function calcular_time(t_list, car_num, manage_time){
    const leng = t_list.length;
    const [in_time, out_time] = [t_list[leng-2], t_list[leng-1]];
    let [hour_i, minute_i] = in_time.split(":");
    let [hour_o, minute_o] = out_time.split(":");
    [hour_i, minute_i, hour_o, minute_o] = [parseInt(hour_i), parseInt(minute_i), parseInt(hour_o), parseInt(minute_o)];
    const i_total = hour_i * 60 + minute_i;
    const o_total = hour_o * 60 + minute_o;
    const total = o_total - i_total;
    
    if (manage_time.has(car_num)){
        let prev_total = manage_time.get(car_num);
        manage_time.set(car_num, prev_total+total);
    }else{
        manage_time.set(car_num, total);
    }
    
    return;
}

function solution(fees, records) {
    const manage = new Map();
    const manage_time = new Map();
    const sort_car_num = [];
    records.forEach((val)=>{
        const [t, car_num, status] = val.split(" ");
        if(manage.has(car_num)){
            const re_val = manage.get(car_num);
            re_val.push(t);
            manage.set(car_num, re_val);
            if(status == "OUT"){
                calcular_time(re_val, car_num, manage_time)
            }
        }else{
            manage.set(car_num, [t]);
            sort_car_num.push(parseInt(car_num));
        }
        
    })
    const full_time = 60*23 + 59;
    for(const [car_num, t_list] of manage){
        if(t_list.length%2 !== 0){
            let [hour, minute] = t_list.at(-1).split(":");
            [hour, minute] = [parseInt(hour), parseInt(minute)];
            const plus_time = full_time - (hour*60 + minute);
            
            if (manage_time.has(car_num)){
                let prev_total = manage_time.get(car_num);
                if( !Number.isInteger(prev_total) ) throw new Error("~~~");
                manage_time.set(car_num, prev_total+plus_time);
            }else{
                manage_time.set(car_num, plus_time);
            }
        }
    }
    
    sort_car_num.sort();
    return calcular_fee(fees, manage_time, sort_car_num);
}