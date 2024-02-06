import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if isPrime(i) == True:
            answer += 1
    return answer

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

#1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
#n	result
#10	4
#5	3
#1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환
