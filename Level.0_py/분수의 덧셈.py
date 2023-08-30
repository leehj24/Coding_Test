def solution(denum1, num1, denum2, num2):
    # 1. 두 분수의 합 계산
    boonmo = num1 * num2
    boonja = denum1 * num2 + denum2 * num1
    
    # 2. 최대공약수 계산
    start = max(boonmo, boonja)
    gcd_value = 1
    
    for num in range(start, 0, -1):
        if boonmo % num == 0 and boonja % num == 0:
            gcd_value = num
            break
    

    # 3. gcd 로 나눈 값을 answer에 담기
    answer = [boonja / gcd_value, boonmo / gcd_value]
    return answer

#또는 
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]

# numer1=3, denom1=4, numer2=2, denom2=8, result=[5,8]