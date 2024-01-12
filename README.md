# SSAFY

# 1월 8일 (월) Robot Quest 복습

1. 주요 용어: 편집창, 콘솔창, 지식베이스
2. 기본값 설정
- from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor
- from spike.control import wait_for_seconds, wait_until, Timer
- from math import “
- hub = Primehub()
- from spike import Motor
- motor = Motor(’C’)
- motor.set_default_speed(100)
- motor.run_to_position(90)
1. 불빛: hub.light_matrix.show_image(’HAPPY’)
2. 두 개의 모터를 동시 제어할 때 사용하는 MotorPair
- pair = MotorPair(’E’,’F’) → 왼쪽 모터가 포트 E에 연결되면 오른쪽 모터는 포트 F에 연결된다.
- **전진 및 후진 : move(거리, 단위, 직진, 속도)**
pair.move(20,’cm’,0,30)
********속도가 음수(-30)면 뒤로 이동한다.********
- **양 바퀴가 동시에 움직이는 탱크 모드 : move_tank(거리/각도/회전횟수/시간, cm/degrees/rotation/seconds,왼쪽모터,오른쪽모터)**
pair.move_tank(20,’cm’,30,30) → (거리, 단위, 왼쪽 모터 속도, 오른쪽 모터 속도)
마찬가지로 속도가 음수(-30)면 후진한다.
- **계속** **전진 및 후진 : start(speed=속도) + wait_for_seconds(초)**
pair.start(speed=50)
wait_for_seconds(3) → 3초 기다리는 동안 로봇은 위 속도로 계속 움직임
pair.stop()
1. 회전
from spike import MotorPair
from spike.control import wait_for_seconds
pair = MotorPair(’E’,’F’)
- **Point turn 제자리회전**
pair.move_tank(720, **‘degrees’**, 30, -30) → (회전각도, 단위, **양 바퀴 반대방향)**
pair.move_tank(2, **‘rotations’**,-30, 30) → (회전횟수, 단위, **양 바퀴 반대방향**)
- **Swing turn 바퀴 한쪽만 회전**
pair.move_tank(720, ‘degrees’, **0, 30**) → 오른쪽 모터만 움직이기 때문에 좌회전
pair.move_tank(2,’rotations’, **30, 0**) → 왼쪽 모터만 움직이기 때문에 우회전
- **Curve turn 양쪽 바퀴 모두 회전**
pair.move_tank(5, **‘seconds’**, 20, 50) → (이동시간, 단위, 양 바퀴 다른 속도로)
1. 모터
- 절대위치: run_to_position()
- 주어진 각도 값: run_for_degrees()
- 지정된 회전 수: run_for_rotations()
- 지정된 초 단위: run_for_seconds()
- 계속지속: start()
- 멈춤: stop()
- 속도 측정: get_speed()
- 절대 위치 측정: get_position
- 회전한 누적 각도 값: get_degrees_counted()
- 현재 기본 속도: get_default_speed()
- 누적 각도 값 설정: set_degrees_counted()
1. 로봇 팔
- 절대위치: motor.run_to_position(90)
- 로봇 팔 위로 올리기: motor.run_for_degrees(-110)
- 로봇 팔 아래로 내리기: motor.run_for_degrees(110)
1. 라이트 매트릭스
- hub = PrimeHub()
hub.light_matrix.show_image(’RABBIT’)
hub.speaker.beep(67, 0.5)
1. **반복문 : while True:**
- while True**:
(TAB) 무한반복할 코드**
1. **특정횟수 반복문: for count in range ():**
2. **조건문 : if 실행조건:**
3. **특정 조건문: elif 실행조건: → 위에 쓴 if가 거짓인 경우에만 실행됨**
4. **조건문 : else:**
5. 거리센서
- 거리 측정
whlie True:
       dist = dist_sensor.get_distance_cm()
- None: 거리를 알 수 없는 경우
       if dist! = None:                      ! = ******************→ ≠****************** 
          print(dist)
- 20cm보다 가까우면 정지, 먼 경우 직진
while True:
       dist = dist_sensor.get_distance_cm()
       if dist ! = None:            or   if dist == None:
           if dist < 20:                         continue
               pair.stop()
          else:
               pair.start(0, 30)
1. 동작센서
- ******************Roll (x축)******************
왼쪽이면 -, 오른쪽이면 +값을 갖는다.
- ************************pitch (y축)************************
위로 올라가면 +, 아래로 내려가면 -값을 갖는다.
- **yaw (z축)
현재 바라보는 방향으로 값 초기화: hub.motion_sensor.rest_yaw_angle()
90도 회전(우): while hub.motion_sensor.get_yaw_angle() < 90**  
                            pair.start_tank(50,0)
                       pair.stop()
**90도 회전(좌): while hub.motion_sensor.get_yaw_angle() > -90**
1. 라인트레이싱
- from spike import ColorSensor, MotorPair
- color = ColorSensor(’A’)
- pair = MotorPair(’E’,’F’)
- while True:
         if color.get_color() == ‘black’ :
            pair.start_tank(35, 20)
         else :
            pair.start.tank(20, 35)

→ 검은 선을 따라 지그재그로 움직이게 된다.

# 1월 9일 (화) creator 복습

[https://create.redbrick.land/class-login?group=CREATE2411](https://create.redbrick.land/class-login?group=CREATE2411)

# 1월 10일 (수) python-1 복습

1. python 설치
2. Git 설치
Git_bash ; 터미널과 관련된 듯 하다.
3. VSCode(***Visual Studio Code***) 설치
    - **마이크로소프트**에서 개발한 코드 에디터의 한 종류
    - 개발자들의 메모장
    - 기존 개발 도구들 보다 **가볍고 빠르다**는 장점
    - Extension을 통해 다양한 기능을 설치할 수 있어서, **무한한 확장성**을 가짐
4. python documentation : 공식문서
5. GPT 챗봇
- API (Application Programming Interface) : 두 SW의 매개체
    
    Interface: 소통 방식. 도구 ex) touch, mouse, keyboard, RC…
    대개 UI가 자주 언급.
    기계 - 기계 소통 방식 → API. 눈에 보이지 않는 영역에서도 소통은 이루어진다. 
    
    Application: 고유한 기능을 가진 모든 SW
    App - App 간 데이터를 얻으려면, **지정된 형식(=API)**에 따라 정보를 요청해야 함.
    
- KEY : 인증된 사용자
    
    But, API에 따라 모든 이에게 준다면 신원 확인 불가. **KEY도 함께 발급하여 사용자 인식 후 정보 제공.** 주민등록증을 발급한 것과 같다. 
    로그인 된 사용자거나, 한 서비스 내에서 이용되는 중이라면 KEY를 따로 발급하지 않기도 한다. 즉, **두 기기 사이**에서만 필요.
    
    
    현재 KEY가 가장 많이 이용되는 영역: “구글로 로그인하기”
    

3개가 함께 챗봇을 구성하게 된다. 

- API_KEY = 요청시 신분증
- OPEN_API_URL = 요청과 신분증을 보낼 주소

- JSON(java)과 DICTIONARY(python)은 구조가 동일함. 이름만 다르다. 
1) { } 중괄호
2) 키 : 값 (p)
- 챗봇이 답변하도록 하기 위해서는
1) **답변 데이터의 위치까지 접근**
2) **변수에 저장** ex. a=3 → 프로그램에서는 3을 그냥 쓸 수 없다. 어딘가로 담아야 한다. 
3) **화면에 출력**
print(p)=console(j)
- 응답을 하나하나 찾아가는 과정

- [ ] = 리스트 = 배열
- 배열 안에 요소가 1개 있을 경우 ‘0’이 나타난다. (프로그래밍에서는 첫 순서가 1이 아닌 0)

# 1월 11일 (목) python-2 복습

## 1. Markdown

- 일반 텍스트로 문서를 작성하는 간단한 방법. 개발자들의 notion임. **코드블럭**을 만들어 낼 수 있다는 게 큰 장점.
- 파일명은 md
- 최종 변환 형태를 확인하기 위해서는 VSC에서 코드를 작성하고 preview로 보면 된다.

### 1. Heading

```java
- 대주제 #
- 중주제 ##
- 소주제 ### 
```

- 소주제부터는 underline이 없다.
- heading은 5(#####)까지 존재.
    
    

### 2. **List**

- 순서가 있는 리스트 (1. 2. 3. 등)
- 순서가 없는 리스트(-)
    
    

### 3. **코드블럭** `

1. code block :`3쌍.
    
    
2. inline code block : 특정 단어 양 옆에 `를 붙이는 것

### 4. **링크 & 이미지**

1. 링크 : [대괄호]
**[링크를 만들고 싶은 단어] (그 옆 소괄호로 url)**
2. 이미지: 느낌표!
**![출력오류시에만 등장하는 대체 텍스트] (다운받은 이미지의 이름 or 온라인상 이미지 주소)**
공유가 되지 않는 주소일 수도 있다. 
이미지의 너비와 높이는 마크다운으로 조절할 수 없음 (html 필요)

### 5. **텍스트 관련 문법**

1. 굵게: 별표 두개 **
2. 기울임: 별표 한개씩*
3. 취소선: 물결표 두개~~

### 6. **수평선** ——— 3개 이상

### 7. **인용문(blockquote)**: 오른쪽 꺽쇠 >

### 8. 기타 Markdown Guide:

[Basic Syntax | Markdown Guide](https://www.markdownguide.org/basic-syntax/)

## 2. CLI(Command Line Interface)

- **명령어**를 통해 사용자와 컴퓨터가 상호작용하는 방식
어제 배운 UI나 API, GUI(**Graphic** User Interface)와 같은 종류.
cf. GUI방식을 처음 도입한 것은 애플. 이전까지는 까만 화면에 코드를 작성하는 것으로 시작.
- GUI대신 CLI를 사용해야 하는 이유?
성능을 줄이기 위함. 현업 개발 시스템은 CLI를 통한 조작 환경 제공. 또 잘 다루면 더 빠르다.
- 내가 어디에 있는지 (경로) 아는 것이 제일 중요!!
    - 절대 경로: Root dir부터 목적 지점까지 거치는 모든 경로를 전부 작성
    ex. C:/Users/ssafy/Desktop
    그러나 깊은 곳에 있을 경우 경로가 너무 길어진다.
    - 상대 경로: ********************내가 있는 dir을 기준으로 계산********************
    현재 C:/Users에 있으면서 ssafy로 이동하고 싶을 때
    ./ssafy 이 상대 경로가 된다. **(현재 위치를 나타내는 ./은 생략이 가능함)**
    또한 ********************************************************************************************************누군가에게 공유하고 싶을 때는 상대 경로를 이용하는 것이 좋다.********************************************************************************************************
- 명령어는 공백을 두고 판단된다.
- 한 줄에 핵심 명령어는 하나.

1. **점 한 개 = 현재 디렉토리(폴더)**
2. **점 두 개 = 상위 디렉토리(폴더)**
************cd ..************ (GUI의 뒤로가기)
3. **새로운 ‘파일’ 만들기**
    
    ```java
    touch
    ```
    
4. **새로운 ‘폴더’ 만들기**
    
    ```java
    mkdir
    ```
    
5. 현재 속한 파일 및 폴더 리스트 보기
    
    ```java
    ls
    ```
    
6. 파일은 확장자명이 뒤에 붙고, **폴더는 /가 뒤에 붙는다.**


7. 다른 폴더로 이동하기
    
    ```java
    cd
    ```
    
8. 현재 위치 확인하기: 경로 확인하기.
    
    
9. 파일 열기
    
    ```java
    start 파일명.형식
    ```
    
10. 파일 지우기
    
    ```java
    rm 파일명.형식
    ```
    
11. 폴더 지우기 = **rm -r** 폴더명
    
    ```java
    rm -r 폴더명
    ```
    
    내부적으로 파일과 폴더의 작동 원리가 전혀 다르기 때문.
    
    
12. 현재위치까지의 절대경로: pwd
13. ~ 모양은 home을 나타냄
14. TIPS
- 하다 보면 화면이 아래로 내려가게 되는데, 1) clear을 입력하거나 2) ctrl+l을 누르면 됨
- 직전에 썼던 명령어를 사용하고 싶으면 ↑ 을 누르기
- 전전에 썼던 명령어를 사용하고 싶으면 ↑↑ 을 누르기
- 가고 싶은 폴더명이 너무 길면 앞에 글자 몇개 입력 후 ****************tab**************** 누르기

## 3. Git → 3단계

- 분산 버전 관리 시스템
    - 버전 관리: **변화/변경사항**을 기록하고 추적.
    전체 내용이 아니라 이전 버전에서 추가된 부분만을 의미. ≠ 저장
    - 버전을 **commit** 이라고 일컫는다. 변경된 파일을 저장하는 것이 사진을 찍듯이 기록한다 하여 ‘snapshot’이라고도 함.
- 코드 히스토리를 관리. 개발되어 온 ‘과정’을 파악.
- 코드의 변경이력을 기록하고 협업을 용이하게 함.
- git은 3가지의 영역이 있는데, invisible. 그래서 좀 어렵대.

1. **영역1: Working Directory**
    - 실제 작업 중인 파일이 위치하는 영역.
2. **영역2: Staging Area**
    - Working dir에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택 추가/제외할 수 있는 중간 준비 영역. not yet 버전. 모든 변경사항이 기록되나 어떤 것만을 버전으로 기록할지 고를 수 있다.
    - 최종으로 확정하려면 꼭 **커밋으로 저장해야 함!!**!
3. **영역3: Repository**
    - 버전 이력과 파일들이 영구히 저장.
    
- 명령어
    1. git 초기화 = **로컬 저장소** 설정
        
        ```python
        git init
        ```
        
        git의 버전 관리를 시작할 디렉토리에서 진행한다.
        git의 영역이라면 경로 뒤에 (master)가 붙는다. 
        

    
    2. Staging Area로 Add하기
        
        ```python
        git add 파일명
        ```
        
        변경사항이 있는 파일을  영역1에서 영역2 staging area에 추가하는 것. 
        현재 디렉토리에 있는 모든 변경사항을 올리고 싶으면 git add . 하면 됨. 
        
    3. Repository에 commit하기
        
        ```java
        git commit -m “버전이름”
        ```
        
        staging area에 있는 파일들을 저장소에 기록 (영역 1인 Working Dir에서 바로 여기로 넘어올 수 없다.)
        
    4. ********************************************************commit 메세지 수정하기********************************************************
        1. 가장 최근 commit 수정하는 법 : 
            
            ```java
            **git commit —amend** → i를 눌러 수정 → **esc - :wq** (저장+창닫기)
            혹은  **git commit —amend -m “수정 메시지”**
            ```
            
        2. 이전 / 여러 commit 수정하는 법 
            
            ```java
            **git rebase -i HEAD~원하는개수**
            수정하고 싶은 commit 옆의  pick → reword로 바꾸기 →  esc - :wq
            ```
            
    5. Author identity를 확보하기 위해 email, 이름 필요.
    **git config**
    global은 pc 전체 범위이므로 다른 파일에서 VSC를 열어도 재설정 필요 없음
    인증 수단으로 사용되지 않으며 서명 정도임
        
        
        Author identity **확인법**
        
        ```java
        **—global —list**
        ```
        
        
        Author 변경하기
        
        ```java
        git commit —amend —author=”이름__ <이메일주소>”
        ```
        
    6. **git status**
    git이 추적하고 있는 파일을 보여준다. 
    GUI가 아니기 때문에 이거 계속 쳐서 확인해야 함.
    
        
        한번 버전 관리가 이루어진 파일은 
        **************************untracked, new file이 아니라 modified가 등장
        이를 Staging Area로 올리면 초록색으로 변함**************************
        
        
    7. **git log**
    
    <aside>
    💡 git 저장소 안에 또 다른  git 저장소는 존재할 수 없다.
    git init을 진행한 상위 디렉토리의 하위 디렉토리 그 어디에서도 git init을 진행하면 안됨. 바깥쪽의 git 저장소가 안쪽의 git 저장소 변경사항을 추적할 수 없기 때문.
    
    만일, desktop에 git init을 했다면, ls -a로 숨김 파일 모두를 드러낸 다음
    
    .git/을 지우면 됨. ************rm -r .git************
    
    
    </aside>
    
    - 글로벌과 로컬
    global(전역) ↔ local(지역)
    cf. local은 online과 반대되는 말로도 쓰인다. remote라는 원격 저장소는 online에 존재.
    - **********************************************git log —oneline : 목록 한 줄로 보기**********************************************

# 1월 12일 (금) python-3 복습

## 1. Remote Repository (원격 저장소)

- 대표적 서비스: GitLab(기업과 사용, 좀 더 private), GitHub, Bitbucket
- VSC 파일명이 “README”일 경우 GitHub에 서문과 같이 나타난다. (*국제적 약속!)

## 2. 로컬 & 원격 저장소

- **로컬 저장소에 원격 저장소 주소 추가하는 법**
    
    ```jsx
    **git remote add 추가하는원격저장소이름 url**
    ```
    
    처음이라면 관행적으로 origin을 사용한다.
    
    별칭은 말 그대로 컴퓨터에서 명령을 하기 위한 나만 보는 거!
    
- 하나의 로컬 저장소에 여러개의 원격 저장소를 등록할 수 있다.
- 원격 저장소 **등록 여부 확인 = 원격 저장소 목록 조회**
    
    ```java
    git remote -v
    ```
    

- 원격저장소에 commit을 올리는 행위 = **push**
    
    ```jsx
    ************************git push -u************************ origin master
    git에 올림  origin이라는 원격저장소에 master라는 가지(branch)를
    ```
    

- 원격저장소에서 내려받는 행위 = **pull(변경사항만큼만** 당겨옴)/ **clone(전체 다** 가져오는 복제행위)
    
    ```python
    ******git pull****** origin master
    ```
    
    - 땡길거야 origin이라는 원격 저장소 master라는 가지에서
    
    ```python
    ******git clone****** 원격저장소url 
    ```
    
    - 전체를 복제해오는 것이기 때문에 저장소 url 자체가 필요하다.
    - clone으로 받은 프로젝트는 이미 git init이 되어 있다.
- push → pull → push → pull 사이클 기억! (업로드 → 다운로드 개념인듯)
- clone할 때는 저장소가 아닌 곳에서 받아야 한다! (**저장소 안에 저장소가 또 존재할 수 없기 때문**)
- Git이 신원 확인차 발급한 자격증명은 윈도우에 **자격 증명**을 검색 → Windows 자격 증명에서 확인할 수 있다. (*자리바꿀 때 이거 지워줘야 함)

## 3. gitignore

- 변경사항을 감지할 필요가 없거나 감지하지 말아야 할 파일, 디렉토리를 추적하지 않도록 설정
- **************************************************************파일 생성 (*확장자 없음)**************************************************************
    
    ```java
    .gitignore
    ```
    
- 먼저 설정해둘 것. ********************************한번 git의 관리를 받은 파일은 이후에 ignore되지 않는다.********************************
- gitignore 설정 서비스
운영체제, 프레임워크, 프로그래밍 언어 등 환경에 따라 gitignore를 만들어주는 사이트
gitignore.io

## 4. github활용

1) 프로젝트 협업

2) 포트폴리오

- TIL (Today I Learned): github repository를 다음과 같은 이름으로 만들어서 성장 내용을 기록하는 것. 단순한 필기가 아니고 자습 내용을 기록.
- 문서화 documentation!! 중욧!!