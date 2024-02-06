def solution(numbers):

    num=[1,2,3,4,5,6,7,8,9]
    a = list(set(num) - set(numbers)) #차집합
    return sum(a) #합계

def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    return answer

#numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return
# arr                  result
# [1,2,3,4,6,7,8,0]	    14
# [5,8,4,0,6,7,9]	    6