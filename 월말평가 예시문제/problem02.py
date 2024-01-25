############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def over(score_list):
    """
    list에 속한 요소를 for문을 통하여 하나씩 뽑아낸 후,
    그 값이 60 이상이라면 로컬 변수인 num을 1씩 증가시키는 방식.
    """
    num = 0
    for score in score_list:
        if score >= 60: 
            num += 1
        else:
            continue
    
    return num
    # 여기에 코드를 작성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
scores1 = [30, 60, 90, 70]
print(over(scores1)) # 3
#####################################################