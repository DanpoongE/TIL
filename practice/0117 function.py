# #함수의 기본 구조
# def greet(name):
#     message = '"Hello, ' + name + '!"'
#     return message

# result = greet('Esther') # -> 이게 함수 호출하는 거!
# print(result)

# # 
# def alarm(time):
#     text = '"It\'s ' + time +'"'
#     return text

# result2 = alarm('11')
# print(result2)

# #
# def day(day):  
#     sentence = '"Today is ' + day +'"'
#     return sentence

# result3 = day('Wednesday')
# print(result3)

# #
# def weather(forecast):
#     text2 = '"Today\'s weather is ' + forecast + '"'
#     return text2

# result4 = weather('snowy')
# print(result4)



# # 내장 함수

# # 절댓값 도출 함수
# print(abs(-13)) #13 바로 도출가능

# # boolean 함수
# empty_list1 = []
# print(bool(empty_list1)) #요소가 없으므로 False

# empty_list2 = [0]
# print(bool(empty_list2)) #요소가 있으므로 True

# print(bool(0)) #숫자 0은 False

# empty_set = {}
# print(bool(empty_set)) #False

# # 정렬 함수
# unsorted_list = ['노', '겨', '후', '타']
# # 1. 
# sorted(unsorted_list) # 위 리스트가 오름차순 배열된다.
# print(unsorted_list) # ['노', '겨', '후', '타']


# #원래 목록이 필요하지 않다면 다음과 같은 방식을 쓰기도 한다.

# unsorted_list2 = ['노', '겨', '후', '타']
# # 2.
# unsorted_list2.sort()
# print(unsorted_list2) # ['겨', '노', '타', '후']


# #그럼 내림차순 배열은 어떻게 할까?
# down = sorted(unsorted_list, reverse=True) #sorted함수의 인자 값에 ,reverse=True를 추가한다!
# print(down)

# # split 함수
# text = "Hello, World!"
# text.split()
# #리턴이 있는지 없는지는 print 해 봐야
# print(text.split()) #['Hello,', 'World!'] -> 리턴이 있음!

# split2 = text.split("H")
# print(split2) #['', 'ello, World!']

# split3 = text.split("l")
# print(split3) #['He', '', 'o, Wor', 'd!']

# # 반복문을 쓴 듯한 map함수
# numbers = [1, 2, 3]
# result = map(str, numbers) #['1', '2', '3']

# print(result)
# print(list(result))

# #zip 함수
# girls = ['jiji', 'ash']
# boys = ['peter', 'jason']
# pair = zip(girls, boys)

# print(pair) #<zip object at 0x000001828AE1AC00>
# print(dict(pair)) #{'jiji': 'peter', 'ash': 'jason'}

#실습 Lv.4 문제
# 1. zip()
# 1.1 일단 zip으로 묶어서 결과 보기
# def create_user(user_info):
#     name, age, address = user_info #인자의 구성 자체를 튜플에서 unpack
#     increase_user()
#     user_info = {
#         'name': name,
#         'age': age,
#         'address': address
#     }
#     print(f'{name}님 환영합니다!')
#     return user_info

# number_of_people = 0


# def increase_user():
#     pass


# def create_user():
#     pass


# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# zip_user = list(zip(name, age, address))
# print(zip_user)

# # 1.2 map 함수를 사용해서 zip으로 묶인 사용자들에게 
# # 각각 create_user 함수를 적용

# result = list(map(create_user, zip_user))
# print(result)
