def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        answer+=A[i]*B[i]
    return answer

def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))

#A리스트와 B리스트의 인자들을 곱하고 더한 값의 최솟값을 찾는 문제입니다.
#A	B	answer
#[1, 4, 2]	[5, 4, 4]	29
#[1,2]	[3,4]	10
