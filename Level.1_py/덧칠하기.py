def solution(n,m,section):
    answer = 1 # 칠하는 횟수
    paint = section[0] # 덧칠 시작점
    for i in range(1, len(section)):
        if section[i] - paint >= m:
            answer += 1
            paint = section[i]
            
    return answer


def solution(n, m, section):
    answer = 0
    paint = 0
    
    for value in section:
        if(value > paint):
            paint = value + m -1
            answer += 1
    
    return answer

#n	m	section	result
#8	4	[2, 3, 6]	2
#5	4	[1, 3]	1
#4	1	[1, 2, 3, 4]	4

#2, 3, 6번 영역에 페인트를 다시 칠해야 합니다. 롤러의 길이가 4미터이므로 한 번의 페인트칠에 연속된 4개의 구역을 칠할 수 있습니다. 
# 처음에 3, 4, 5, 6번 영역에 페인트칠을 하면 칠해야 할 곳으로 2번 구역만 남고 1, 2, 3, 4번 구역에 페인트칠을 하면 2번 만에 다시 칠해야 할 곳에 모두 페인트칠을 할 수 있습니다.

