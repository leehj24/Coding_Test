def solution(s):
    arr = s.split(' ')
    result =[]
    for i in arr :
        if i=='Z':
            result.pop()
        else:
            result.append(int(i))
    return sum(result)

# 문자열에 있는 숫자를 차례대로 더하려고 합니다. 이 때 "Z"가 나오면 바로 전에 더했던 숫자를 뺍니다
# 숫자와 "Z"로 이루어진 문자열 s가 주어질 때, 머쓱이가 구한 값을 return 합니다.

# s="12Z3" ,result=4 //1+3=4