def convert(n, base):
        arr = "0123456789ABCDEF"
        q, r = divmod(n, base)
        if q == 0:
            return arr[r]
        else:
            return convert(q, base) + arr[r]
    
def solution(n, t, m, p):
    answer = ''
    test = ''
    
    for i in range(m*t):
        test += str(convert(i, n))
        
    while len(answer) < t:
        answer += test[p-1]
        p += m
        
    return answer

print(solution(2,4,2,1))