def solution(a,b,n):
    answer =0
    while n>=a:
        remain=n%a
        n=(n//a)*b
        answer+=n
        n+=remain
    return answer

def solution(a, b, n):
    answer = 0
    while n >= a:
        answer += ((n // a) * b)
        n = (n % a) + ((n // a) * b)
    return answer

#타풀이
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b

# a병에 b만큼 병을 준다 하였을 때 n병일 경우 얼마큼 병을 받는지에 대한 return값
#a	b	n	result
#2	1	20	19
#3	1	20	9