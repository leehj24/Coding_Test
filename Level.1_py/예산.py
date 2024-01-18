def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
        else:
            break
    return answer
# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록
# d	            budget	result
#[1,3,2,5,4]	9	    3
#[2,2,3,3]	    10	    4

#1원, 3원, 5원을 신청한 부서의 물품을 구매해주려면 9원이 필요합니다

