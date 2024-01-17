a = 1
b = 2

def enclosed(a):
    c = 3

    def local(c):
        print(a, b, c) #(100, 2, 500)

    local(500)
    print(a, b, c) #(100, 2, 3)


enclosed(100)
print(a, b) #(1, 2) -> 일 것 같은데... 14번째 줄은 enclosed 영역이고, 
#15번째 줄은 글로벌 영역이라는 걸 어떻게 알 수 있지?? 
#함수가 정의되는 영역이 중요??