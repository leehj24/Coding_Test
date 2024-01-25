def coke(k,m,p):
    answer = 0 
    score = sorted(p, reverse = True)
    for i in range(0, len(score), m):
        tmp = score[i:i+m]
        if len(tmp) == m:
            answer += min(tmp) * m
        
        
    return answer

def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m

# k = 3, m = 4, 사과 7개의 점수가 [1, 2, 3, 1, 2, 3, 1]이라면, 
# 다음과 같이 [2, 3, 2, 3]으로 구성된 사과 상자 1개를 만들어 판매하여 최대 이익을 얻을 수 있습니다.
# k	 m	score	                                result
# 3	 4	[1, 2, 3, 1, 2, 3, 1]	                8
# 4	 3	[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]	33
                