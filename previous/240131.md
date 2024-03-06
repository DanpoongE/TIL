1. 유효범위 적는법: if 0<=ni<N and 0 <= nj<N: 
2. 2차원 배열(필수암기): arr = [list(map(int, input().split())) for _ in range(N)]
3. int를 더하기
   - sum(iter)이기 때문에, int는 sum으로 합을 더할 수 없다
   - level초보: int를 new_list에 모아 sum(new_list)해주기
   - level고수: 아무변수a=0을 할당하고, a += int 해주기
4. tc 숫자 print해야 될 때
   - 그냥 시작하면 0부터라 표현이 귀찮아
   - for tc in range(1, T + 1): 라고 해주면 tc바로 1부터 시작.
5. 연속되었는가?
   - count = 0 으로 해두고 target number가 나오면 +1을 해주다가, 시리즈가 끊기면 다시 count = 0으로 리셋하는 방법.
6. 