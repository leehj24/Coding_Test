def coke(k,score):
    answer = []
    a=[]
    for i in score:
        if len(a)<k:
            a.append(i)
        else:
            if min(a)<i:
                a.remove(min(a))
                a.append(i)
        answer.append(min(a))              
    return answer

def solution(k, score):
    answer = []
    temp = []
    for i in score:
        temp.append(i)
        temp.sort(reverse=True)
        temp = temp[:k]
        answer.append(min(temp))
    return answer


#일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.

# 일차          1   2      3     4    5    6     7  
# score        10   100   20    150   1   100   200
# k(명예전당)   10   100   100   150  150  150   200
#                    10    20   100   100  100  150
#                          10   20    20   100  100
# 발표점수      10    10    10   20    20   100  100

# k     score                                           result
# 3     [10, 100, 20, 150, 1, 100, 200]                 [10, 10, 10, 20, 20, 100, 100]
# 4     [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]   [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]