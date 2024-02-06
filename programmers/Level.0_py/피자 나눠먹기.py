def solution(n):
    return (n - 1) // 7 + 1
#또는 
def solution(n):
    answer = 0

    if n%7 != 0:
        answer = (n//7) + 1
    else:
        answer = n//7

    return answer
#피자 한판에 7조각이다 n명수라면 몇판을 시켜야 하는가
# n=15 result=3