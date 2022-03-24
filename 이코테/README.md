### import module  
import 순서  
1. sys.modules
2. built-in modules
3. sys.path  

기본적으로 export 따로 코드없고 같은 폴더에 위치하면 import module 로 바로 사용가능  

하위폴더 모듈 import 경우: `from 절대경로.모듈 import 함수, 클래스`  

상위폴더 모듈 import 경우: 모듈 폴더 위치 sys.path.append 해주고 `import 모듈` 로 사용가능  

상대 경로는 `ImportError: attempted relative import with no known parent package` err발생, 상위폴더의 경우 __main__을 기준으로 위치를 잡아서 실제 폴더구조를 근거하지 않는다고 함 그래서 경로로 import 불가  

---
### sys.stdin.readline()
_여러줄의 입력을 받아야 하는 경우가 아니라면 sys없이 input() 으로도 충분하다._  

이렇게 받으면 개행문자 \n가 포함된체 받아진다.  
ex) `"hi\n"`  
그러나 split()하면 개행문자는 없는 취급된다.  

문자열로 받을거면: 
```
sys.stdin.readline().rstrip()
```  
split 붙일거면: 
```
input = sys.stdin.readline 
input().split()
```
이런 느낌으로 활용하면 된다.  
rstrip()은 개행문자를 없애준다.  

### 삼항연산자
on_true if 조건 else on_false  

python 삼항연산자에서 변수 재할당안된다.  
`++, --` 같은 증감연산자도 없어서 `+=` 로 보통 재할당하는 걸 못쓴다.  
파이썬 삼항연산자는 동작 수행보다 반환값을 제공하는 용도로만 쓰는 듯 하다.  

### tuple 
특징: 내부 값이 변하지 않는다.  

### list _(주의)_
```
[0] * 4 = [0, 0, 0, 0]
[] * 4 = []
```
list의 상수곱은 열 의 개수를 늘려준다.  
_빈 리스트에는 적용되지 않는다._  

```
a = ['a', 'b', 'c', 'd', 'e']

|  0  |  1  |  2  |  3  |  4  |  
| -5  | -4  | -3  | -2  | -1  |  

# a[-2] = 'd'  
```
음수 슬라이스  

### shallow/deep copy  
그냥 코딩하면 얕은 복사가 되고 mutable한 자료형의 얕은 복사는 원본을 변경할 수 있다.  
_list, set, dict는 mutable하다._

원본과 분리된 변수를 위해 다음 모듈을 사용한다.
```
import copy

a = [1,2,3,4,5]
b = copy.deepcopy(a)
c = copy.copy(a)
```
`copy()`가 `deepcopy()`보다 빠르게 동작하나 `copy()`는 배열의 내부 객체까지 깊은 복사를 하지 않는다.  
_즉 이중 이상의 배열은 깊은 복사가 이뤄지지 않음_  

1차원 리스트를 제외하고는 `deepcopy()`를 사용하자.  

_JS에도 해당되는 내용이며 JS도 자료형에 따라 복사하는 방법이 있다._

### map  
사용 예:
+ list(map(함수, 리스트))
+ tuple(map(함수, 튜플))  

map은 리스트 요소를 지정된 함수로 처리하고 원본 대상을 변경하지 않고 새 객체를 생성한다.  
리스트, 튜플 뿐 아니라 모든 반복 가능한 객체를 처리할 수 있다.  
str 예시:  
+ list(map(int, "101100"))  
출력: [1, 0, 1, 1, 0, 0]  

변수 할당안하고 map()만 쓰면 실행안된다.  
_list(map())은 할당안해도 실행됨_

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
### set 
+ 중복을 허용하지 않는다.
+ 순서가 없다.
+ 인덱싱 접근은 리스트나 튜플로 변환후에 가능하다.
```
aa = set([1,4,56,56,9,9,1,2,0,4])
# {0, 1, 2, 4, 9, 56}

bb = set("hello")
# {'o', 'l', 'e', 'h'}
```
### list method  
`list.index(찾는 값) :` list에서 찾고자 하는 값과 일치하는 첫번째 index값 반환, 없으면 ValueError  
`list.count(찾는 값) :` list에서 찾고자 하는 값의 개수를 반환, 없으면 0반환  

---
`if문` 이나 `for문`은 또다른 스코프를 형성하는게 아니라 그냥 해당스코프에서의 동작이다.  

### 문자열 method
양쪽 끝과 이어진 특정 문자들 삭제 _( 끝에서 떨어지면 삭제 안됨, 한 문자 단위로 삭제 )_
```
a = [1,2,3]

b = a.strip("[]")
print(b) # 1,2,3 
```
문자열 삭제/치환 _( 양쪽 끝과 무관하고 문자열 단위로 삭제/치환 )_
```
text = "ariaabc"

text1 = text.strip("abc")
print(text1) # ri

text2 = text.replace("abc","")
print(text2) # aria
```
둘 다 새로운 str으로 반환한다는 점을 주의하자. _( 원본은 그대로 )_
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
### sorted(sort)  
sort()와 sorted()는 모두 정렬하기 전에 각 리스트 요소에 대해 호출할 함수를 지정하는 key 매개 변수를 가지고 있다.    
예시:
```
students = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]

sorted(students, key = lambda student: student[2])

# 출력: [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
예시와 같이 students 요소의 [2]항목을 기준으로 sorted 됐다. _( 10, 12, 15 순으로 )_  

sort는 알파벳도 정렬할 수 있다.  
단, list method이므로 str이 아니라 list형이여야 한다.

### lambda  
함수를 정의할 필요없이 사용하고 싶을 때 쓴다.  
```
lambda 매개변수 : 리턴값   #함수 정의와 같다.

(lambda 매개변수 : 리턴값)(매개변수 값) #함수 정의 + 실행과 같다. 
```
### not A
논리연산자이며  
A가 True면 False 반환  
A가 False면 True 반환

### 문자열 method
`isalpha()`: 문자열 구성이 __모두__ 알파벳이면 True, 아니면 False _( 숫자, 기호, 공백 등 )_  
`isdigit()`: 문자열 구성이 __모두__ 숫자면 True, 아니면 False _( 알파벳, 기호, 공백 등 )_   
`isalnum()`: 문자열 구성이 __모두__ 숫자 or 알파벳 이면 True, 아니면 False _( 기호, 공백 등 )_ 

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
