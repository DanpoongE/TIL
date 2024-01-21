# built-in function
1. `sum()`
   - 주어진 (list,tuple,range,set)의 `값`을 모두 더할 때 쓰는 함수
   - 값이니까 int가 아닌 str은 안됨~
   - **정해지지 않은 개수의 인자를 더할 때는 `*args`를 쓰면 된다**
   - ![Alt text](image.png)  
2. `bool()`
   - `bool(변수명)`
   - (안에는 int, list 등 가능)
   - `bool(0)` 과 `bool([0])`은 같지 않다. 각각 F / T 도출됨
3. `abs()`
   - 절댓값을 도출하는 함수
4. `sorted()`
   - 오름차순 정렬. 원본은 바뀌지 않는 채, return값으로 정렬된 새로운 리스트가 나온다.
   - `변수명.sort()`도 오름차순 정렬하는 방식인데, 이 친구는 `return값이 없다. 즉, 원본 자체가 바뀌기 때문에` 오름차순 된 결과를 얻고 싶으면 `print(변수명)`을 호출하면 된다. 
5. `sorted(변수명, reverse=True)`
   - 내림차순 정렬.
6. `sep()`
7. `reversed(seq)`
8. `변수명.split()`
   - ()을 기준으로 나눈다. 공백이라면 str 공백을 기준으로, 다른 문자라면 해당 문자 전부를 기준으로 원본이 나뉘게 된다.