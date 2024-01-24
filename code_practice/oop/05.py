class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.add_count()

    @classmethod # 무언가를 기능적으로 더해주는 함수 
    def number_of_population(cls):
        # cls는 class 자기 자신x. 클래스 메서드를 호출하는 class. class 자기 자신이 아닌 이유는 class는 상속이 되기 때문.
        print(f'인구수는 {cls.count}입니다.')
        # 이 def만 보면 count 누구껀지 모름..! 호출할 때 알게 됨. 

    # +1 하는 클래스 메서드
    def add_count(cls):
        cls.count += 1


person1 = Person('iu')
person2 = Person('BTS')
Person.number_of_population()  # 인구수는 2입니다.
