인접 행렬만 가지고 있을지, 전체 행렬 가지고 있을지는 방법의 차이 방법이 바뀌어도 __풀이의 알고리즘은 그대로다.__  
_근데 적절한 행렬 방식을 취할때와 안취할 때 차이가 큰 문제들이 꽤 있다._ 

선택한 행렬에서 좀 꼬인다 싶으면 다른 행렬로 유연하게 바꿔 생각하자. 꼬인다 싶으면 적절하지 않을 확률이 높음

---
if in (N), remove (N), pop (N) 시간복잡도 안좋다. 되도록 지양하자  

enumerate 쓰다보면 가독성이 별로인 것 같다. range로 통일해 쓰자