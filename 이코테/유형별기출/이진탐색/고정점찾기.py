import sys
input =sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def unit_point(arr, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        a = unit_point(arr, start, mid-1)
        if a: return a
        b = unit_point(arr, arr[mid]+1, end)
        if b: return b
    elif arr[mid] < mid:
        a = unit_point(arr, start, arr[mid]-1)
        if a: return a
        b = unit_point(arr, mid+1, end)       
        if b: return b

result = unit_point(arr, 0, len(arr)-1)
if result:
    print(result)
else:
    print(-1)