n = int(input())
arr = set(map(int, input().split()))	# 탐색 시간을 줄이기 위해 set으로 받음
k = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr:
        print(1)
    else:
        print(0)