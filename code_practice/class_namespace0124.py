class Person:
    name = 'unknown'
    # 초기값을 넣을 게 없기 때문에 작성하지 않기도 한다.

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk() # 본인한테 없는 instance 변수는 class에서 찾아 쓴다.

p2 = Person()
p2.name = 'kim'
p2.talk()

# p2.talk('yoon') -> 'unknwon과 yoon 두개의 위치 인자를 받았다고 생각.

p2.ssafy = 11
print(p2.ssafy) #p1이랑은 전혀 관계가 없다는 건 알겠당. ++설명추가,