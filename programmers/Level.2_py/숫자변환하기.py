def solution(x, y, n):
    answer = 0
    dp = set()
    dp.add(x)
    
    while dp:
        if y in dp:
            return answer
        else:
            dp_y = set()
            for i in dp:
                if i+n <= y:
                    dp_y.add(i+n)
                if i*2 <= y:
                    dp_y.add(i*2)
                if i*3 <= y:
                    dp_y.add(i*3)
            dp = dp_y
            answer += 1
            
    return -1

print(solution(10,40,5))

# x	    y	n	result
# 10	40	5	2
# 10	40	30	1
# 2	    5	4	-1

# 자연수 x를 y로 변환하려고 합니다. 

# x에 n을 더합니다
# x에 2를 곱합니다.
# x에 3을 곱합니다.

# 자연수 x, y, n이 매개변수로 주어질 때, x를 y로 변환하기 위해 필요한 최소 연산 횟수를 return 
# 이때 x를 y로 만들 수 없다면 -1을 return 해주세요.