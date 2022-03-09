## 선택정렬
arr = [7, 5, 9, 1, 4, 5, 2, 11]

for i in range(len(arr)):
    m_index = i
    for j in range (i+1, len(arr)):
        if arr[j] < arr[m_index]:
            m_index = j
    arr[i], arr[m_index] = arr[m_index], arr[i]

print(arr)

## 삽입정렬
arr = [7, 5, 9, 1, 4, 5, 2, 11]

for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
        else:
            break
        
print(arr)
