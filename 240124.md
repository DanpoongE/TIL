1. 들어가기 전에...
- 인스턴스 함수 작성시 `(self)` 꼭꼭꼭 넣어주세여 꼮이여~!
2. 인스턴스와 인자 (feat. 생성자함수)
- 인스턴스 생성시 인자를 넣을 거라면 `인스턴스명=class(인자)`, 생성자함수를 넣어야 한다 `def __init__(self, 인자명): // self.인자명 = 인자명`. 
- 인스턴스 생성시 `인스턴스명=class()`와 같은 형태라면 class 내 인스턴트 메서드 함수를 정의할 때 매개변수로 함께 정의해주면 된다 `def 인스턴트메서드함수명(self, 인자): // self.인자명 = 인자명` .
- 즉, 생성자 함수 `매개변수` -> 인스턴스 생성 시 인자 넣겠다. 

1. 예시 
- class Circle:

    def __ init __(self, r): 

    self.r = r            
    
    def notice(self):
        
    return f'이 원의 반지름은 {self.r}입니다.'
    
    c1 = Circle(5) # 인스턴스 생성시에 r값을 부여

    c1.r # 5

1. 예시2
- class Circle:
  
  def notice(self, r):

    self.r = r
    
    return f'이 원의 반지름은 {self.r}입니다.'

    c1 = Circle()

    print(c1.notice(5))

    print(c1.r)


4. 인스턴스가 생성될 때마다 클래스 변수가 늘어나도록 만들기
- ![Alt text](image-4.png)
- 클래스변수: number_of_people
- 생성자 함수 영역에서 `클래스명.클래스변수 연산자`를 활용하면 된다.
  
5. 용어
- `클래스 속성` (ex. bloodtype = 'red')
- `인스턴스 변수` (ex. self.width = width)

6. 내장함수
- `dir()` : 메서드 목록 출력

7. _ str _ 매직 메서드
- class 안에 또 다른 인스턴스 메서드 이름을 지을 필요 없다. 
- 즉, print시 `print(변수명.인스턴스메서드)` 라고 할 필요가 없다는 거. `print(변수명)`이라고 하면 출력된다. 