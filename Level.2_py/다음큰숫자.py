
def solution(n):
    answer = 0
    one_count = bin(n).count("1")
    
    for num in range(n+1, 1000001):
        num_one_count = bin(num).count("1")
    
        if one_count == num_one_count:
            answer = num
            break
        
    return answer
    
    
def solution(n):
    c = n+1
    while True:
        if bin(c).count('1') == bin(n).count('1'):
            return c
        c += 1

#연속된 자연수들로 n을 표현하는 방법의 수
#n  answer
#78 83
