
N, M = map(int, input().split())
adj = {i: i for i in range(1, 101)}

for _ in range(N + M):
    x, y = map(int, input().split())
    adj[x] = y

# 리스트를 큐로 사용
q = [(1, 0)]  # 초기값 (현재 위치, 이동 횟수)
visited = [False] * 101
visited[1] = True

while q:
    pos, step = q.pop(0)  # 큐의 첫 번째 요소를 꺼냄

    if pos == 100:
        print(step)
        break

    for i in range(1, 7):  # 주사위 눈 1~6
        next_pos = pos + i
        if next_pos > 100:
            continue

        next_pos = adj[next_pos]  # 사다리나 뱀을 타고 이동

        if not visited[next_pos]:
            visited[next_pos] = True
            q.append((next_pos, step + 1))  # 큐에 추가

##############################################


## 다른풀이

from collections import deque

N, M = map(int, input().split())
adj = {i: i for i in range(1, 101)}

for _ in range(N+M):
    x, y = map(int, input().split())
    adj[x] = y

q = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while q:
    pos, step = q.popleft()

    if pos == 100:
        print(step)
        break

    for i in range(1, 7):
        next = pos + i
        if next > 100:
            continue

        next = adj[next]

        if not visited[next]:
            visited[next] = True
            q.append((next, step+1))

