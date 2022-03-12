n, target = map(int, input().split())
arr = list(map(int, input().split()))

## 오름차순 정렬 됐다 가정
def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            start = mid + 1

        if arr[mid] > target:
            end = mid - 1
    return None

result = binary_search(arr, target, 0, len(arr)-1)
if ( result == None ):
    print(" target이 없습니다 ")
else:
    print(arr[result],'(은)는',"[%d] 인덱스 입니다."%result)