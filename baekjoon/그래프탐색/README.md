__[2178_미로탐색](./2178_%EB%AF%B8%EB%A1%9C%ED%83%90%EC%83%89.py)__  
dp없이 visited를 deep copy하면 동일 시점 같은 count의 경로도 모두 계속 탐색한다. 시간하고 메모리 둘 다 초과  

## copy.deepcopy
사용하지 말자 slicing이 정답
```
e.g)

O copy_list = [item[:] for item in origin_list]

X copy_list = [item for item in origin_list]
# 얕은 복사임 주의
```
slicing이 시간은 해결해줘도 메모리는 여전히 많이 먹는다. 되도록 이런 시점에서는 dp적인 생각을 해보자.