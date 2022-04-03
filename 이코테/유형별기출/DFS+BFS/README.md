## 주의
ex) 3 < n,m < 9  
n따로 m따로가 아니라 n과 m 두 변수의 범위가 3과 9사이에 있다는 뜻  

체크할 요소 많아지면 시간차이 조금 생긴다. 되도록이며 논리연산자 적게 나오는 쪽으로 코딩하자  

## Python
전역 변수 함수에서 그냥 쓰는 건 가능  
전역 변수에 재할당은 런타임 에러  _( 재할당 할거면 global 쓰기 )_  
ex)
```
a = 1
def test():
    a + 1
    return a
# 1
```
재할당은 안하고 이렇게 연산만 취하면 에러는 없으나 생각대로 동작 안함 _( 주의 )_  

```
def test():
    return "abc", ""

a, b = test()
# 위에 처럼 받으면 b가 할당없다고 err난다.

yap = test()
# 이렇게 받으면 ("abc", "") 으로 들어가 있다.
```
할당으로 받을 때는 None이 없게 주의하자.  
```
text = "hello"
text[0] = "g"
# err난다.

text2 = list(text)

text = str(text2)
# err는 없으나 안바뀐다 그대로 리스트다.

text = ''.join(text2)
# join 메서드를 사용해야 한다.
# 앞의 '' 는 list element들 사이에 기호를 추가할 수 있다.

text = ','.join(text2)
# h,e,l,l,o
```
str은 원소를 바꿀 수 없다.  
list to str 은 join 메서드를 이용하자.