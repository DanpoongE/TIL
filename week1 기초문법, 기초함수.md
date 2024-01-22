# 0115 기초 문법
1. 표현식expression < 문장statement
- 표현식: 값, 변수, 연산자 등을 조합하여 계산, 결과를 내는 코드 구조
- 문장: 실행 가능한 동작을 기술하는 코드
- 문장은 보통 여러 개의 표현식을 포함한다. 
2. 변수명 규칙
- 영문 알파벳, _, 숫자로 구성
- 숫자로 시작할 수 없음
- 대소문자 구분
3. 주석처리
- #(샾처리)
- 여러 줄 주석 ''' '''
4. 변수에 재할당
    - number = 10
    
        double = 2 * number
        
        print(double)  # 20
        
        number = 5
        
        print(double)  # **20** -> 여전히 double은 20의 주소를 참고
5. str을 표현하는 ' '은 print시 나타나지 않는다.
6. str * int = 'str''str'... 으로 출력됨
7. 변수가 많을 때 한 문장으로 표현하려면 f-string을 쓰는 게 편하다.
8. 같은 data type끼리는 연산자 활용 가능
9. index 거꾸로 출력하기 (slicing) [::-1]
10. 제곱(**), %을 함께 쓸 때 먼저 계산해야 하는 건 ( )처리
11. print(aa, bb) -> aa bb와 같이 두 변수 사이에 빈칸이 있는 채로 출력된다. 
12. 데이터 타입 확인법
    - `print(type(변수))` -> <class`데이터타입`>
# 0116 기초 문법2
1. sequence type 중 `list`만 유일하게 순서 변경 가능
2. 단축평가
- 효율적인 계산을 위하여 모든 연산을 진행하지 않고, and의 경우 전자가 F이면 F를, or의 경우 전자가 T이면 T를 도출하는 것을 말함.
3. 형변환
- list를 set으로 변환하는법 : `a = [list]`를 다음과 같이 재할당한다. `a = set(a)` 
- 이때 set{}가 아닌 `set()`로 표현한다. 함수이기 때문. 
- int, float도 가능
4. 세트의 집합 연산
- 합집합 |
- 차집합 -
- 교집합 &
5. 멤버십 연산자
- in, not in 
# 0117 함수와 제어문 1
1. 함수의 정의와 호출
- 함수는 필요한 경우 결과를 반환`return`할 수 있다.
- **return문은 함수의 실행을 종료**하고, 결과를 호출 부분에서 반환한다. 
- 함수는 호출 시점이 중요하다! 순서대로 정의되지 않더라도 호출시 있으면 도출됨!
2. 함수의 return
- 어떤 함수가 return이 있는지 없는지는 함수 호출 후 원본이 변했는지 변하지 않았는지를 보면 된다. 변했다면 return이 없고, 변하지 않았다면 리턴이 있다.
- 다른 확인법으로는 해당 함수를 print해 보는 방법이 있다. print(변수명.함수())했을 때, None이라면 return이 없고, 어떤 값이 나오면 return이 있다!
2. 인자의 종류
    
    a. 위치인자: 함수 호출 시 반드시 값을 전달해야 한다.

    b. 기본 인자 값 : 정의 시 매개변수에 값을 할당하는 것. 호출 시 값을 전달하지 않으면 매개변수에 할당된 값이 출력된다. **위치인자 뒤에 와야 한다**

    c. 키워드 인자 : 호출 시 인자의 이름과 값을 함께 전달. 순서에 관계없이 특정 매개변수에 값을 할당할 수 있다. **반드시 위치 인자 뒤에 위치해야 한다**

    d. 임의의 인자 : 정의 시 `*args`로 

    e. 임의의 키워드 인자 : 정의 시 `*kwargs`로 표현, 호출 시 **딕셔너리** 형태로 나타남. 
3. 함수 인자 작성 권장 순서 : 위치 -> 기본 -> 가변 -> 가변 키워드 
4. map 함수: `map(적용할func, iterable)`
5. zip 함수: `zip(*iterables)` -> 튜플로 나옴
6. lambda 함수: `lambda 매개변수 : 표현식`
7. packing: 변수에 담긴 값들은 print시 튜플로 pack. `*b`는 남은 요소들을 리스트로 패킹하여 할당
8. unpacking 
- 튜플이나 리스트 등의 객체 요소들을 개별 변수에 할당. `a, b, c, d, e = 객체 요소 하나하나` -> `print(a, b, c, d, e)` 
- 리스트의 경우, `print(*리스트명)`을 통해 언팩할 수 있다. 
- 딕셔너리의 경우, `딕셔너리키값 함수명print(**딕셔너리명)`을 통해 언팩할 수 있다.

# 0118 함수와 제어문 2
1. 모듈 가져오기
- `from A import B` : A라는 패키지/모듈에서 B라는 모듈/함수(또는 변수)를 가져오겠다.
- 다른 패키지X의 모듈Y에서 Z함수(또는 변수) 불러오기: `from X.Y import Z`
- `import C as D` : C라는 모듈/함수를 D라는 이름으로 쓰겠다. 
- 모듈에 무엇이 들어있는지는 `help(모듈명)`을 통해 확인 가능하다.

2. 반복문
- `for`문은 리턴 없이 쓰고 print할 것.
- 딕셔너리 순회: `for key in dict: print(key), print(dict[key])` 하면 key와 value값이 차례로 등장한다.  

3. 새로운 리스트 만드는 법
- ![how_to_make_list](image-2.png)
6. 리스트 안 10개의 딕셔너리에서 'name' value값만 가져오기
- `for i in range(10)` -> in 다음에 값이 포함된 리스트명이 올 수도, 범위값이 올 수도 있다. 둘 다 iter 이기 때문!
- 설정한 다른 리스트에 값 넣기: 먼저 빈 리스트 선언 `emtpy_list = []`후 `for`문과 `append`로 해결할 수 있다. 
- `for i in range(10)`
    - `empty_list.append(원래data[i]['name])
    - `print(empty_list)`하면 되어 있음!
    - `어디에.append(무엇을)` = 앞에 있는 곳에 넣겠다. 

7. 두 리스트 비교하기
- list1 == list2 # True, False
- 리스트가 정렬되지 않은 상태라면 False가 나올 수 있다! 그땐 `sorted()`를 통해 비교가능 `sorted(list1)==sorted(list2)`

8. 딕셔너리 값을 함수 호출시 인자로 쓰는 방법
- unpacking: **으로 처리한다.
- function(arg1, arg2, arg3)
- dict{arg1:aaa, arg2:bbb, arg3:ccc}여서 dict의 key값이 바로 function 인자에 들어갈 수 있을 경우, `function(**dict)=fuction(aaa, bbb, ccc)`가 됨.

9. list comprehension
- `expression for 변수 in iterable`

10. enumerate(iterable, start=0)
- iterable 각 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수