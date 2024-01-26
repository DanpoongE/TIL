1. `.count()` 는 리스트에서만 사용 가능하다. 
   - 다른 type의 경우 list로 형변환이 필요하겠쬬?
   - 각 타입별 메서드 잘 기억하자!
2. index
   - seq는 각각 두개의 index를 부여받는다. 
   - max = len() - 1
3. `''.join(reversed(str))`
   - `reversed()` 내장 함수를 쓴다
   - 그대로 출력하면 <0x0021300>이런게 뜬다. 메모리에 저장된 상태이나 내가 읽을 수 없는 상태. 
   - 이 경우 `''.join()`을 통해 구분자 없이 하나의 문자열로 나타나도록 한다. 
4. int() 형변환
   - int(float나 str)만 가능
5. for문, print 한줄로 쓰기
   - print(result, `end=' '`) 라고 `end=''`를 붙여주면 된다. 
   - end의 작은따옴표 사이에는 구분자를 넣어주면 된다. 출력되는 값 사이사이에 들어가면 좋겠는거!
6. l.append와 l.extend
   - extend는 `(iterable)` 한 게 오느냐 안오느냐를 묻는 질문에 잘 쓰임. 따라서 ([요소1개짜리list]) 를 잘 기억할 것!! 이거 과제 5번에서 쓰인당.
7. pop과 for
   - for문에선 원래 iterable의 길이 조작 금지!
   - pop을 쓰면 list가 자꾸 줄어들어서 고정된 횟수만큼의 반복이 어려워진다.
   - while + list가 빌 때까지 반복
   - while len(list_data) > 0 
8. `for i in range(len(list))` -> range 수만큼 돈다!
9. if문에서 `.isdecimal()`과 같은 true/false를 뱉어내는 메서드를 쓴 경우
   - true면 if문이 실행되고, false면 elif나 else로 넘어간다!  