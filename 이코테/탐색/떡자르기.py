import sys

n, m = map(int, input().split())
input_data = sys.stdin.readline().rstrip()
input_data = list(map(int, input_data.split()))

start = 0
end = max(input_data)

while start <= end:
    hap = 0
    cut_len = (start + end)//2
    for i in input_data:
        if (i - cut_len > 0):
            hap += (i-cut_len)

    if hap == m:
        print(cut_len)
        break
    if hap > m:
        start = cut_len + 1
    if hap < m:
        end = cut_len -1