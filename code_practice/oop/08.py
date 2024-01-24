class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

    # 인스턴스를 print할 때 결과로 나오는 값을 결정
    def __str__(self):
        return f'[원] radius: {self.r}'


c1 = Circle(10)
c2 = Circle(1)

print(c1.area())

print(c1)  # [원] radius: 10
print(c2)  # [원] radius: 1
