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


text = "Hello, World!"
text.split()
#리턴이 있는지 없는지는 print 해 봐야
print(text.split()) #['Hello,', 'World!'] -> 리턴이 있음!

split2 = text.split("H")
print(split2) #['', 'ello, World!']

split3 = text.split("l")
print(split3) #['He', '', 'o, Wor', 'd!']













# def greet(name, age):
#     print(f'안녕하세요, {name}님! {age}살이시군요.')

# greet(age=30, name='Bella')


# # greet('Alice', 25)
# # greet('Alice', 25, 'AAA')

# def func(pos1, pos2, age=30, *args, **kwargs):
#     print(pos1, pos2, age, args, kwargs)

# func(1, 2, 3, a=100, b=200)

# # 반복문을 쓴 듯한 map함수
# numbers = [1, 2, 3]
# result = map(str, numbers)

# print(result)
# print(list(result))