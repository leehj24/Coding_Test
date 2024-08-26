from collections import deque

def solution(prices):
    new = deque(prices)
    answer = []
    while new:
        price = new.popleft() 
        sec = 0
        for q in new:
            sec += 1
            if price > q:
                break
        answer.append(sec)
        
    return answer

##

def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution([1,2,3,2,1]))