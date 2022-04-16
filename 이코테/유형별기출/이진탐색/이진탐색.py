import sys
input =sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search_left(arr, target, start, end):
    while end >= start:
        mid = (start + end)//2
        if mid == 0 and arr[mid] == target:
            return mid
        elif arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

def binary_search_right(arr, target, start, end):
    while end >= start:
        mid = (start + end)//2
        if mid == len(arr)-1 and arr[mid] == target:
            return mid
        elif arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

first = binary_search_left(arr, x, 0, len(arr)-1)
last = binary_search_right(arr, x, 0, len(arr)-1)
if first == None:
    print(-1)
else:
    result = last - first + 1
    print(result)