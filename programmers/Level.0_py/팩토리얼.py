def solution(n):
    answer = 1
    fac=1
    while fac<=n:
        answer +=1
        fac =fac*answer
    answer=answer-1
    return answer
#또는 
from math import factorial
def solution(n):
    k = 10
    while n < factorial(k):
        k -= 1
    return k

# n=3628800	,result=10 //10!=10*9*8*7*6*5*4*3*2*1=3628800
# i!<=n 이 되는 i으 ㅣ최대 숫자를 return