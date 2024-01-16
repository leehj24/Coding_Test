def solution(x):

    Sum=sum(int(i) for i in str(x))
    if x%Sum ==0:
        return True
    else:
        return False
    
def solution(n):  
    return n % sum([int(c) for c in str(n)]) == 0

#양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 
#예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 


