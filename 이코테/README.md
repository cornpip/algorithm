## import module  
import 순서  
1. sys.modules
2. built-in modules
3. sys.path  

기본적으로 export 따로 코드없고 같은 폴더에 위치하면 import module 로 바로 사용가능  

하위폴더 모듈 import 경우: `from 절대경로.모듈 import 함수, 클래스`  

상위폴더 모듈 import 경우: 모듈 폴더 위치 sys.path.append 해주고 `import 모듈` 로 사용가능  

상대 경로는 `ImportError: attempted relative import with no known parent package` err발생, 상위폴더의 경우 __main__을 기준으로 위치를 잡아서 실제 폴더구조를 근거하지 않는다고 함 그래서 경로로 import 불가  

---
### 삼항연산자
on_true if 조건 else on_false  

python 삼항연산자에서 변수 재할당안된다.  
`++, --` 같은 증감연산자도 없어서 `+=` 로 보통 재할당하는 걸 못쓴다.  
파이썬 삼항연산자는 동작 수행보다 반환값을 제공하는 용도로만 쓰는 듯 하다.  

### tuple 
특징: 내부 값이 변하지 않는다.  

### map  
사용 예:
+ list(map(함수, 리스트))
+ tuple(map(함수, 튜플))  

map은 리스트 요소를 지정된 함수로 처리하고 원본 대상을 변경하지 않고 새 객체를 생성한다.  
리스트, 튜플 뿐 아니라 모든 반복 가능한 객체를 처리할 수 있다.  
str 예시:  
+ list(map(int, "101100"))  
출력: [1, 0, 1, 1, 0, 0]

### Dictionary
for문
```
a = {'alice': [1, 2, 3], 'bob': 20, 'tony': 15, 'suzy': 30}

for key in a:
    print(key)
    # 출력: alice, bob, tony, suzy

for val in a.values():
    print(val)
    # 출력: [1,2,3], 20, 15, 30

for key, val in a.items():
    print(key,value)
    # 키와 값 모두 사용가능
```

### list method  
`list.index(찾는 값) :` list에서 찾고자 하는 값과 일치하는 첫번째 index값 반환, 없으면 ValueError  
`list.count(찾는 값) :` list에서 찾고자 하는 값의 개수를 반환, 없으면 0반환  

---
`if문` 이나 `for문`은 또다른 스코프를 형성하는게 아니라 그냥 해당스코프에서의 동작이다.  

### Comprehension  
한 Sequence가 다른 Sequence (Iterable Object)로부터 (변형되어) 구축될 수 있게한 기능이다.  
+ List Comprehension
```
# [출력표현식 for 요소 in 입력Sequence [if 조건식]]

oldlist = [1, 2, 'A', False, 3] 
newlist = [i*i for i in oldlist if type(i)==int]

print(newlist)
# 출력: [1, 4, 9]
```
+ Set Comprehension
```
# {출력표현식 for 요소 in 입력Sequence [if 조건식]}

oldlist = [1, 1, 2, 3, 3, 4]
newlist = {i*i for i in oldlist}
 
print(newlist)
# 출력 : {16, 1, 9, 4}
```
+ Dictionary Comprehension
```
# {Key:Value for 요소 in 입력Sequence [if 조건식]}

id_name = {1: '박진수', 2: '강만진', 3: '홍수정'}
name_id = {val:key for key,val in id_name.items()}

print(name_id)
# 출력 : {'박진수': 1, '강만진': 2, '홍수정': 3}
```  

---
### 주의  
```
while ~:
    for i in ~:
        ...
        continue 
        ...
```
continue는 바로 위의 루프로 돌아간다. _( 위의 예시에서 for로 돌아가 진행한다. )_  
```
while ~:
    for i in ~:
        ...
        break
        ...
```
break은 바로 위의 루프 _( while, for )_ 를 탈출한다.
```
    def1():
        ...
        def2():
            ...
            return
```
위의 경우 return은 def2에서의 탈출이다.  

### 스와프  
```
    array[0], array[1] = array[1], array[0]
```
이게 당연해보여도 사실 그렇지 않은게 `array[0] = array[1]` 이 먼저 동작했다면 `array[1] = array[1]` 꼴이 되는 거다.  
python에서 동작되는 코드라 생각하자.  

_%) JS에선 `const a, b = 1, 2` 이런식으로 선언도 안되고 당연 스와프도 안된다._  
_%) `const [a, b] = [1, 2]`_ 이런식은 가능
