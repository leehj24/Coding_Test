def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2): 
        for j in range(i+1, len(nums) - 1): 
            for k in range(j+1, len(nums)): 
                if check(nums[i], nums[j], nums[k]): answer += 1
    return answer 

#또는 

from itertools import combinations 
def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    A = list(combinations(nums, 3))
    for i in A: 
        if check(i[0], i[1], i[2]): answer += 1
    return answer

#또는

class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer

# 개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다.
# nums              result
# [1, 2, 3, 4]      1
# [1, 2, 7, 6, 4]   4