
def sol(n,k):
    word =""
    while n:
        word = str(n%k)+word
        n=n//k
    word = word.split("0")
    
    count = 0
    for i in word:
        if len(i)==0:
            continue
        elif len(i)<2:
            continue
        sosu=True
        for j in range(2,int(int(i)**0.5)+1): # 소수찾기
            if int(i)%j==0:
                sosu=False
                break
        if sosu:
            count+=1
    return count
print(sol(437674,3))


##또는 

def is_prime(num):
    if num < 2:  # 소수는 2 이상만 가능
        return False
    for i in range(2, int(num**0.5) + 1):  # 2부터 √num까지 나눠보기
        if num % i == 0:
            return False
    return True

def solution(n, k):
    # n을 k진수로 변환
    result = "" 
    while n > 0:
        remin = n % k  
        result = str(remin) + result  
        n //= k  

    # 변환된 k진수를 "0"을 기준으로 분할
    answer = result.split("0")
    
    # 소수 개수 세기
    r = 0
    for i in answer:
        if i and is_prime(int(i)):  # 빈 문자열 제외하고 소수인지 판단
            
            r += 1
    return r



# 자연수n을 k진수로 변환한 수 숫자 0인 기준으로 수를 나누어 소수인 수의 개수를 return
# n	k	result
# 437674	3	3
# 110011	10	2