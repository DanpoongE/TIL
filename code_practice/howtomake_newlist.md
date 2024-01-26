
5. 새로운 리스트 만드는 법
   - ![how_to_make_list](image-2.png)
6. 리스트 안 10개의 딕셔너리에서 'name' value값만 가져오기
   - `for i in range(10)` -> in 다음에 값이 포함된 리스트명이 올 수도, 범위값이 올 수도 있다. 둘 다 iter 이기 때문!
   - 설정한 다른 리스트에 값 넣기: 먼저 빈 리스트 선언 `emtpy_list = []`후 `for`문과 `append`로 해결할 수 있다. 
   - `for i in range(10)`
     - `empty_list.append(원래data[i]['name])`
     - `print(empty_list)`하면 되어 있음!
     - `어디에.append(무엇을)` = 앞에 있는 곳에 넣겠다. 

8. 두 리스트에 공통적으로 들어있는 요소 새로운 리스트로 정리하기
   - common = []
   - for compo in list11:

            if compo in list22:
                common.append(compo)
    ![list comparison](image-1.png)