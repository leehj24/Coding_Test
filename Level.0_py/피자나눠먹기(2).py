import math
def solution(n):
    return (n * 6) // math.gcd(n, 6) 

#또는 
def solution(n):
    answer = 1
    while answer * 6 % n != 0:
        answer += 1
    return answer


