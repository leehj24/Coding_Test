# k = int(input())
# n = [i for i in range(1,k+1)]

# while len(n)>1:
#     n.pop(0)
#     n.append(n.pop(0))
# print(n[0])

from collections import deque

k = int(input())
n = deque(range(1, k+1))
print(n)
while len(n) > 1:
    n.popleft()           # 맨 앞의 값을 버림
    n.append(n.popleft()) # 맨 앞의 값을 뒤로 이동

print(n[0])               # 마지막 남은 값 출력
