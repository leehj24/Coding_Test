def solution(numlist, n):
    numlist = sorted(numlist, reverse = True)
    numlist = sorted(numlist, key = lambda x : abs(n-x))
    return numlist

def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer

# 정수 n을 기준으로 n과 가까운 수부터 정렬하려고 합니다. 이때 n으로부터의 거리가 같다면 더 큰 수를 앞에 오도록 배치합니다. 
# 정수가 담긴 배열 numlist와 정수 n이 주어질 때 numlist의 원소를 n으로부터 가까운 순서대로 정렬한 배열을 return하

# numlist	                        n	    result
# [1, 2, 3, 4, 5, 6]	            4	    [4, 5, 3, 6, 2, 1]
# [10000,20,36,47,40,6,10,7000]	    30	    [36, 40, 20, 47, 10, 6, 7000, 10000]