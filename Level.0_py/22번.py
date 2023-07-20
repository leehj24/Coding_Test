def solution(a, b, c):
    answer = 0
    if a==b and b==c and c==a:
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a!=b and b!=c and c!=a:
        answer = a+b+c
    else:
        answer = (a+b+c)*(a**2+b**2+c**2)
    return answer
#세 숫자가 모두 다르다면 a + b + c 점을 얻습니다.
#세 숫자 중 어느 두 숫자는 같고 나머지 다른 숫자는 다르다면 (a + b + c) × (a2 + b2 + c2 )점을 얻습니다.
#세 숫자가 모두 같다면 (a + b + c) × (a2 + b2 + c2 ) × (a3 + b3 + c3 )점을 얻습니다.