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
## 삼항연산자
on_true if 조건 else on_false  

python 삼항연산자에서 변수 재할당안된다.  
`++, --` 같은 증감연산자도 없어서 `+=` 로 보통 재할당하는 걸 못쓴다.  
파이썬 삼항연산자는 동작 수행보다 반환값을 제공하는 용도로만 쓰는 듯 하다.