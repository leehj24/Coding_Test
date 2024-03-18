
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

# 자연수n을 k진수로 변환한 수 숫자 0인 기준으로 수를 나누어 소수인 수의 개수를 return
# n	k	result
# 437674	3	3
# 110011	10	2