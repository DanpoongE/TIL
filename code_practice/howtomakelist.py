numbers = ['1', '2', '3']
# => [1, 2, 3]으로 바꾼 새로운 리스트 생성

# 1. 일반 for 문
new_numbers = []

for num in numbers:
    new_numbers.append(int(num))   
    # list comprehension에서는 이 줄의 최종 변환 형태인 int만 써주면 됨


print(new_numbers)

# 2. map 함수
new_numbers2 = list(map(int, numbers))
print(new_numbers2)

# 3. list comprehension
new_numbers3 = [int(num) for num in numbers]
print(new_numbers3)