N = int(input())

array = []
for i in range(N):
    a = int(input())
    array.append(a)

array.sort()

for i in array:
    print(i)

#################위에꺼 메모리 초과됨;;;

import sys

MAX = 10001
counts = [0] * MAX

n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(MAX):
    for _ in range(counts[i]):
        print(i)


""" 숫자 입력한 n 만큼 다른숫자 입력 후 오름차순으로 print"""