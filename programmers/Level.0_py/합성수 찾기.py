def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
#또는
def solution(n):
    answer = 0 ;c = 0
    for i in range(n+1):
        for j in range(1, i+1):
            if i % j == 0:
                c += 1
        if c >= 3:
            answer += 1
    return answer


# 약수의 개수가 3인 이상인 수를 합성수라 하는데 n이하의 합성수의 개수를 return
# n=10 result =5 //합성수=4, 6, 8, 9, 10