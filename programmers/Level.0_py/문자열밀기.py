def solution(A, B): 
	return (B * 2).find(A)

def solution(A, B):
    answer = -1
    ## 처음부터 A와 B가 같으면
    if A==B:
        return 0
    for i in range(1, len(A)) :
        ## A를 오른쪽으로 한 칸씩 밀었을때
        A = A[-1]+A[0:-1]
        print(A)
        if A == B:
            return i  
    return answer


# 문자열 A와 B가 매개변수로 주어질 때, A를 밀어서 B가 될 수 있다면 밀어야 하는 최소 횟수를 
# return하고 밀어서 B가 될 수 없으면 -1을 return 하도록 solution 함수를 완성해보세요.

# A	            B       result
#"hello"	"ohell"	      1
#"apple"	"elppa"	     -1
#"atat"	    "tata"	      1
#"abc"	    "abc"	      0