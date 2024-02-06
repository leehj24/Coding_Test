import math
def solution(arr):      
    answer = arr[0]
    for n in arr:
        answer = (n * answer) // math.gcd(n, answer)
    return answer

    
def coke(arr):
    m=max(arr)
    while True:
        c =0
        for i in arr:
            if m % i == 0:
                c += 1
            else:
                break
        if c == len(arr):
            break
        m += 1
    return m

print(coke([2,6,8,14]))

# 배열 n수의 최소공배수를 구하여라
# n	             result
# [2,6,8,14]	 168