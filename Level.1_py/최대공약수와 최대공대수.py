def solution(n, m):
    # 최대 공약수 구하기
    for i in range(min(n, m), 0, -1):
        if (n % i == 0) and (m % i == 0):
            a = i
            break
    # 최소 공배수 구하기        
    for j in range(max(n, m), (n * m) + 1):
        if j % n == 0 and j % m == 0:
            b = j
            break
    return [a, b]

def solution(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]
    return answer

def solution(a, b):
    for i in range(a):
        if a%(a-i)+b%(a-i) == 0:
            return [a-i, a*b/(a-i)]

#두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수
# n   m   return
# 3  12   [3, 12]
# 2   5   [1, 10]
