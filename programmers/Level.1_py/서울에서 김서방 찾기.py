def solution(x):

    Sum=sum(int(i) for i in str(x))
    if x%Sum ==0:
        return True
    else:
        return False
    
def solution(seoul):
    a = [i for i,j in enumerate(seoul) if j == "Kim"]
    answer = "김서방은 "+ str(a[0])+ "에 있다"
    return answer

def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))

#String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, 
#예를 들어 ["Jane", "Kim"] "김서방은 1에 있다"
