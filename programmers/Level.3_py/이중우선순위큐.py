import heapq
def solution(operations):
    q = []
    
    for i in operations:
        x,num = i.split()
        num = int(num)
        
        if x == "I":
            heapq.heappush(q,num)
            
        elif x == "D" and num ==1:
            if len(q) !=0:
                num_max = max(q)
                q.remove(num_max)
        else:
            if len(q)!=0:
                heapq.heappop(q)
    if len(q)==0:
        return [0,0]
    else:
        return [max(q),heapq.heappop(q)]
print(sol(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

# 배열 원소에 I가 잇으면 뒤 숫자는 추가, D면 큐에서 최댓값을 삭제 D -면 큐에서 최소값을 삭제한다. 
# 이때 이중 우선순위 큐가 할 연산 operations가 매개변수로 주어질 때, 모든 연산을 처리한 후 큐가 비어있으면 
# [0,0] 비어있지 않으면 [최댓값, 최솟값]을 return