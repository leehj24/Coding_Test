def solution(a, b):
    answer = 0
    if a %2!=0 and b%2!=0:
        answer+=a**2+b**2
    elif a %2==0 and b%2==0:
        answer=abs(a-b)
    else:
        answer=2*(a+b)
    return answer
#a와 b가 모두 홀수면 a제곱 +b제곱   
#a와 b가 모두 짝수면 절대값(a-b)
#둘중 하나만 홀수면 2*(a+b)
#a=3 b=5 result = 34