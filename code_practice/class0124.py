class Person:
    # 속성 = 변수
    blood_color = 'red'

    def __init__(self, name):
        self.name = name
    
    def singing(self):
        return f'{self.name}가 노래합니다.'

# 클래스에서 인스턴스 생성    
singer1 = Person('hi')
singer2 = Person('BTS')

# 매서드 호출 (현재 2개가 있지만, instance가 쓸 수 있는 건 매직메서드 제외한 거!)
# 인스턴스.메서드
print(singer1.singing())
print(singer2.singing())

# 인스턴스.속성(변수)
print(singer1.blood_color)
