def solution(arr):
    stk = []
    idx = 0
    
    while idx < len(arr):
        if len(stk) == 0:
            stk.append(arr[idx])
            idx += 1
        elif len(stk) > 0 and stk[-1] < arr[idx]:
            stk.append(arr[idx])
            idx += 1
        elif len(stk) > 0 and stk[-1] >= arr[idx]:
            stk.pop()
    
    return stk
 
# 만약 stk가 빈 배열이라면 arr[i]를 stk에 추가하고 i에 1을 더합니다.
#stk에 원소가 있고, stk의 마지막 원소가 arr[i]보다 작으면 arr[i]를 stk의 뒤에 추가하고 i에 1을 더합니다.
#stk에 원소가 있는데 stk의 마지막 원소가 arr[i]보다 크거나 같으면 stk의 마지막 원소를 stk에서 제거합니다.

# i	 arr[i]	stk
# 0	  1	    []
# 1	  4	    [1]
# 2	  2	    [1, 4]
# 2	  2	    [1]
# 3	  5	    [1, 2]
# 4	  3	    [1, 2, 5]
# 4	  3	    [1, 2]
# -	  -	    [1, 2, 3]