1. 정규표현식
   - import re
   - pattern = abcd
   - text = abelskdfevsabcdabcd
   - `print(re.findall(pattern, text))` -> abcd 겹치는 거 list 형태로 다나온다.
2. 문자열 내에서 특정 문자열 개수 찾기
   - `s.count(txt)`
3. 문자열의 문자들을 분리하여 리스트로 변환하는 법
   - str = "ddd"
   - new_list = `list(str)`
4. `input().split()`을 하는 이유는 문자열 사이사이에 있는 공백을 제거하기 위해서
5. `map(함수, 객체)`의 경우 map은 객체 요소 하나하나에 함수를 적용하겠다는 뜻임
6. `break` for문 끝에 break 써주면 한번만 돌고 끝난다.
7. 문자열 split
   - `banana bana`의 경우 a, b = input().split() 하면 
8. 빈 set 만들기
   - a = set()
   - {}인데 딕셔너리로 인식하기 때문
9.  set 메서드
   - list는 append나 extend / set은 add!
10. unpacking
   - f-str은 함수가 아니라 내부에서 언패킹을 할 수 없다. 
   - print는 함수라 unpacking 가능!
11. 