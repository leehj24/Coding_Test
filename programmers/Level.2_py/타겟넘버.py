def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 
# 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
# 이때 만들수 있는 경우의 수의 개수를 return 

# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
# [4, 1, 2, 1]	    4	    2
