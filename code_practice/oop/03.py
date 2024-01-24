# class Person:
#     count = 0

#     def __init__(self, name):
#         self.name = name
#         Person.count += 1


# person1 = Person('iu')
# person2 = Person('BTS')

# print(Person.count)  # 2


class Circle:
    pi = 3.14

    def __init__(self, r): # 생성자 함수 -> 인스턴스 생성시에 인자 넣겠다. 
        self.r = r            
    
    # def notice(self):
    #     return f'이 원의 반지름은 {self.r}입니다.'


c1 = Circle(5) # 인스턴스 생성시에 넣겠다.
# c2 = Circle(10)
c1.r

print(c1.notice())



# 



class Circle:
    pi = 3.14

    # # r = f'이 원의 반지름은 {r}입니다.'
    # 이 메서드에서 받은 r을 인스턴스 변수 r로 저장하고
    # 이 인스턴스 변수 r을 출력
    def notice(self, r):
        self.r = r
        return r
    
c1 = Circle()
# 
print(c1.notice(5))
print(c1.r) # 5  인스턴스 변수 r을 생성하도록 하세욥!
