def solution(x, n):
    
    answer = [  ]
    for i in range (1,n+1):
        answer.append(x*i)  
    return answer

def solution(x, n):
    return [x*i for i in range(1, n+1)]

# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴
# x	    n	answer
# 2	    5	[2,4,6,8,10]
# 4	    3	[4,8,12]
# -4	2	[-4, -8]

