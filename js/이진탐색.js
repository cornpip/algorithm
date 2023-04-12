function binarySearch(input, target, start, end){
    input = input.sort();
    let mid = parseInt((start + end)/2);    
    if( mid == start || mid == end ) return mid;
    
    if ( input.at(mid) == target ) return mid;

    if ( input.at(mid) > target ) return binarySearch(input, target, start, mid);

    if ( input.at(mid) < target ) return binarySearch(input, target, mid, end);
}

const input = [1,3,5,7,9];
const res = binarySearch(input, 5, 0, input.length-1);
console.log(res);