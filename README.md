1. 행렬에서 가장자리 값을 포함시키지 않는 경우: `for i in range(1, N-1)`, `for j in range(1, N-1)` 로 지정해주면 더 좋다...!
2. list 요소 하나하나 풀어주는 방법: `print( , end='')`, `unpack *`
3. sort와 sorted()의 차이
   - `l.sort()`는 리스트형의 메소드. 원본값을 직접 수정한다.
   - `sorted(l)`은 내장함수로서 원본은 건드리지 않고 정렬 값을 반환한다. 
4. `sorted(iterable, /, *, key=None)` -> 상우 코드 참고
5. `repr()` 함수는 변수 또는 객체의 고유 표기 정보를 문자열로 만듦. 
6. `if str1 in str2:`
7. `find` 메서드는 char의 index를 찾아주는 함수에오. 없으면 -1이오.