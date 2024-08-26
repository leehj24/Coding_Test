import heapq

def solution(scoville, K):
    answer = 0
    
    while scoville[0]<K:
        news = heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville,news)
        answer +=1
        
        if scoville[0]<K and list(scoville)==1:
            return -1
        
    return answer

print (solution([1, 2, 3, 9, 10, 12],7))