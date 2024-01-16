# 1월 16일 파이썬 기초 문법
1. data type
- 수 : int, float -> 형변환시 다음과 같은 함수로 사용할 수 있다. int(), float()
- sequence : str, list, tuple, range
  - 순서있음. index로 특정 요소만 불러낼 수 있다. `**변수명[index]**`
  - list만 유일하게 변경가능
  - range는 반복문, list와 함께 쓰여 다음과 같은 형태를 띤다. `print(list(range변수명))`
- non-sequence : dict, set
  - 순서없음. index가 아닌 `key`로 특정 요소만 불러낼 수 있다. 

2. 단축평가
- 효율적인 계산을 위하여 모든 연산을 진행하지 않고, and의 경우 전자가 F이면 F를, or의 경우 전자가 T이면 T를 도출하는 것을 말함.
- 값이 '존재'하면 True, '없으면' False. 
  
3. 형변환
- list를 set으로 변환하는법 : `a = [list]`를 다음과 같이 재할당한다. `a = set(a)` 
- 이때 set{}가 아닌 `set()`로 표현한다. 함수이기 때문. 
- 그러니까 set은 non-sequence 타입이기도 하면서 함수로도 사용이 가능한거!
4. range
- range(n): 0부터 **n-1**까지의 숫자 시퀀스
- range(n, m-1): n부터 m-1까지
- **range에도 index 0부터가 적용됨. 끝부분 m-1**
- range를 list로 출력하기 위해서는, `변수x = range(범위)`로 설정하고 print시 list함수 써주기. `print(list(x))`
5. 리스트 특정 요소를 조합하여 문장 만들기
- 콤마로 잇기 `the_list[index1], "string" , the_list[index2]`
- f-string으로 잇기 `f'{the_list[index1]} string {the_list[index2]}}`
6. 