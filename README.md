1. def 함수 시 print, return의 차이
   - print()는 함수다. 그러니까 반복돼
   - return은 def된 함수를 끝내는 거. 
   - print(print(1)) -> 우선 `print(1)=1`이 출력되고 그 프린트 함수 반복되면서 return이 더이상 없음 -> 이걸 바깥의 print()가 받아서 'None'값이 출력됨.
2. d.setdefault(k[,v])의 기능
   - setdefault는 key에 해당하는 `value를 찾을 수 있고`
   - 없는 key는 value와 함께 dict에 추가한다. 
   - 이때 d.setdefault 메서드 자체를 print하면 `추가된 v`가 나오고
   - dict를 print하면 `v가 추가된 dict`가 나온당
3. print(set)
   - 배열 순서가 계속 바뀐다. 순서가 없기 때문에.
4.  