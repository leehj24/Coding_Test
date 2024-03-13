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
            

# 입출력 예
# priorities	        location	return
# [2, 1, 3, 2]	        2	            1
# [1, 1, 9, 1, 1, 1]	0	            5

# 예를 들어 프로세스 4개 [A, B, C, D]가 순서대로 실행 대기 큐에 들어있고, 
# 우선순위가 [2, 1, 3, 2]라면 [C, D, A, B] 순으로 실행하게 됩니다.

# 현재 실행 대기 큐(Queue)에 있는 프로세스의 중요도가 순서대로 담긴 배열 priorities와, 
# 몇 번째로 실행되는지 알고싶은 프로세스의 위치를 알려주는 location이 매개변수로 주어질 때, 
# 해당 프로세스가 몇 번째로 실행되는지 return 하도록 solution 함수를 작성해주세요.

# 예제 #2
# 6개의 프로세스 [A, B, C, D, E, F]가 대기 큐에 있고 중요도가 [1, 1, 9, 1, 1, 1] 이므로 [C, D, E, F, A, B] 순으로 실행됩니다. 따라서 A는 5번째로 실행됩니다.

