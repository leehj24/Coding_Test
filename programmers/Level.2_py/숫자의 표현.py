def solution(n):
    answer=0
    for i in range(1,n+1):
        test=0
        for j in range(1,n+1):
            test +=i
            if test==n:
                answer+=1
                break
            elif test>15:
                print("hj",j)
                break
    return answer
    
def solution(n):
    return len([i  for i in range(1,n+1,2) if n % i is 0])

#연속된 자연수들로 n을 표현하는 방법의 수
#n  answer
#15 4

#1 + 2 + 3 + 4 + 5 = 15,  4 + 5 + 6 = 15,  7 + 8 = 15 , 15 = 15