def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer

# 정수 배열 'numbers'가 모든 원소에 대한 뒷 큰 수들을 차례로 담은 배열을 return  단, 뒷 큰 수가 존재하지 않는 원소는 -1을 담습니다.
# numbers	            result
# [ 2, 3, 3, 5 ]	    [ 3, 5, 5, -1 ]
# [ 9, 1, 5, 3, 6, 2 ]	[ -1, 5, 6, 6, -1, -1 ]