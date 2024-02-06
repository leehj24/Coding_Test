def solution(left, right):
    answer = 0
    for i in range(left, right+1):	
        now_count = 0		
        for j in range(1, i+1):		
            if i % j == 0:		
                now_count +=1	
                
        if now_count % 2 == 0:		
            answer += i			
        else:
            answer -= i			
            
    return answer

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
# 정수 left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록
#left	right	result
# 13	17	    43
