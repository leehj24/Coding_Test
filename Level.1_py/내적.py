def solution(a,b):
    answer = 0
    for i in range(len(a)):
        answer += a[i]*b[i]
    return answer

def solution(a,b):
    return sum([x*y for x, y in zip(a,b)])
# a 와 b의 내적은 a[0]*b[0]+a[1]*b[1]+...a[n]*b[n]이다
# a         b          result
# [1,2,3]   [-1,0,1]    2
# [1,0,1]	[-1,4,5]    4