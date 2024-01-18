def solution(n):
    answer = ''

    while n >= 0:			
        n, re = divmod(n,3)	
        answer += str(re)
    return int(answer, 3)
        
print(solution(45))
# n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return
# n    (3진법)	 앞뒤반전(3진법)	10진법으로 표현
# 45	1200	    0021	            7
