from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2

# 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
# 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을, 
# 무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

#   a	b	result
#   7	20	1
#   11	22	1
#   12	21	2