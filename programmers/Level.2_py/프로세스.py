from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque(priorities)
    names = deque()
    for i in range(len(queue)) :
        names.append(chr(ord('A')+i))
    alp = names[location]
    
    while alp in names :
        back = False
        x = queue.popleft()
        y = names.popleft()
        for q in queue :
            if x < q :
                queue.append(x)
                names.append(y)
                back = True
                break
        if back == False :
            answer += 1
    return answer

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
            
def solution(p, l):
    ans = 0
    m = max(p)
    while True:
        v = p.pop(0)
        if m == v:
            ans += 1
            if l == 0:
                break
            else:
                l -= 1
            m = max(p)
        else:
            p.append(v)
            if l == 0:
                l = len(p)-1
            else:
                l -= 1
    return ans      
            
# priorities	        location	return
# [2, 1, 3, 2]	        2	           1
# [1, 1, 9, 1, 1, 1]	0	           5

# 예제1
# 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 
# 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 예제 #2
# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [
# 1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 
# 따라서 A는 5번째로 실행됩니다.