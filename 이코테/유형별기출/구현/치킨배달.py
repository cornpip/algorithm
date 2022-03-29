from itertools import combinations
import sys
input = sys.stdin.readline

def check(village):
    chick = []
    home = []
    leng = len(village)
    for i in range(1, leng):
        for j in range(1, leng):
            if village[i][j] == 1:
                home.append((i,j))
            elif village[i][j] == 2:
                chick.append((i,j))
    return [chick, home]

n, m = map(int, input().split())
village = [["x"]] 

for _ in range(n):
    village.append(["x"] + list(map(int, input().split())))

chick, home = check(village)

if(len(chick) >= m):
    final_result = int(1e9)
    for i in combinations(chick, m):
        result = 0
        for ho in home:
            ho_chi = int(1e9)
            for chi in i:
                dx = abs(ho[0] - chi[0])
                dy = abs(ho[1] - chi[1])
                # print(ho, chi, dx, dy)
                if (dx+dy) < ho_chi: ho_chi=(dx+dy)
                # print(ho_chi)
            result += ho_chi 
        if result < final_result: final_result = result

print(final_result)