def test(i ,cnt, stop):
    cnt.append(i)
    i += 1
    if stop == 3:
        return
    print("first", cnt, stop)
    test(i, cnt, stop+1)
    print("second", cnt, stop)
test(0,[], 1)

## list자료형의 매개변수는 재귀함수에 영향을 받는다. == 전역변수 처럼 동작한다.

def test2(cnt, stop):
    cnt = not cnt
    if stop == 3:
        return
    print("first", cnt, stop)
    test2(cnt, stop+1)
    print("second", cnt, stop)
test2(True, 1)

def test3(cnt, stop):
    cnt += "_ "
    if stop == 3:
        return
    print("first", cnt, stop)
    test3(cnt, stop+1)
    print("second", cnt, stop)
test3("", 1)

# string, boolean자료형은 재귀함수에 영향을 받지않는다. == 지역변수 처럼 동작

# js도 동일하게 동작한다.