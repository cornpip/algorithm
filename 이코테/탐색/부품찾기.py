import sys

n = int(input())
n_data = sys.stdin.readline().rstrip()
n_data = list(map(int, n_data.split()))

m = int(input())
m_data = sys.stdin.readline().rstrip()
m_data = list(map(int, m_data.split()))

# 정렬 후 이진탐색
# n_data.sort()
# def binary_search(arr, target, start, end):
#     while start <= end:
#         mid = (start + end)//2
#         if arr[mid] == target:
#             return "yes"
#         if arr[mid] > target:
#             end = mid - 1
#         if arr[mid] < target:
#             start = mid + 1
#     return "no"

# for i in m_data:
#     print(binary_search(n_data, i, 0, len(n_data)-1), end=" ")

# 계수 정렬
# arr = [0] * 1000001
# for i in n_data:
#     arr[i] = 1

# for i in m_data: 
#     if arr[i] == 1:
#         print('yes', end=" ")
#     else:
#         print('no', end=" ")

# 집합 자료형 이용
for i in m_data:
    if i in n_data:
        print('yes', end=" ")
    else:
        print('no', end=" ")
# M * 탐색 시간복잡도 일텐데 (시간복잡도 모름)


# 근데 (현재복잡도=정렬+탐색에서) 둘 다 큰 비중을 차지하고 있기에
# 둘 중 하나를 뺄 수 없을까 하는 접근을 알아두자 
# 메서드 이용이나 계수정렬이 그런 접근이다.