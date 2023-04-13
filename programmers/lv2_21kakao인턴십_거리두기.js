/**
 *  3<=i<5 안됨 ( 양쪽비교 python만 된다. )
 */
function around(row, col, table2) {
    for (let i = row - 1; i <= row + 1; i++) {
        for (let j = col - 1; j <= col + 1; j++) {
            if (i < 0 || j < 0 || i > 4 || j > 4) continue;
            if (i == row && j == col) continue;

            if (table2[i][j] == "P") {
                let dist = Math.abs(row - i) + Math.abs(col - j);

                if (dist == 2) {
                    if (row > i) {
                        if (table2[row - 1][col] == "X" && table2[i + 1][j] == "X") continue;
                        return false;
                    } else if (row < i) {
                        if (table2[i - 1][j] == "X" && table2[row + 1][col] == "X") continue;
                        return false;
                    }
                } else return false;
            }
        }
    }

    let p_p = [[0, -2], [0, 2], [1, -2], [1, 2]];
    for (let i of p_p) {
        let [a, val] = i;
        let r, c;
        if (a == 0) {
            r = row + val;
            c = col;
        } else {
            r = row;
            c = col + val;
        }

        if (r < 0 || r > 4 || c < 0 || c > 4) continue;
        if (table2[r][c] == "P") {
            if (a == 0) {
                if (table2[r - (val / 2)][c] == "O") return false;
            } else {
                if (table2[r][c - (val / 2)] == "O") return false;
            }
        }
    }
    return true;
}

function solution(places) {
    let ans = places.map((place) => {
        let res = 1;
        let table = new Array(5).fill(0).map((v) => {
            return new Array(5).fill(0);
        });

        let table2 = place.map((v) => v.split(""));

        let q = [[0, 0]];
        while (q.length > 0) {
            let [r, c] = q.shift();
            // console.log(r,c);
            if (table[r][c] == 1) continue;
            else table[r][c] = 1;

            if (table2[r][c] == "P") {
                if (around(r, c, table2) == false) {
                    res = 0;
                    break;
                }
            }

            if ((r + 1) <= 4) q.push([r + 1, c]);
            if ((c + 1) <= 4) q.push([r, c + 1]);
        }
        return res;
    })
    return ans;
}

const tc1 = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]];

const tc2 = [["POOPO", "OOOOO", "OOOXP", "OPOPX", "OOOOO"]];
const res = solution(tc2);
console.log(res);