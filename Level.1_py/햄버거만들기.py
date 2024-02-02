def coke(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer
        
    
print(coke([2,1,1,2,3,1,2,3,1]))

# 햄버거는 [빵-야채-고기-빵]순이여야한다. 빵은1,야채2,고기3 일때 햄버거를 만들수 있는 수를 return
# ingredient	                result
# [2, 1, 1, 2, 3, 1, 2, 3, 1]	2