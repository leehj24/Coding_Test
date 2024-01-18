def solution(s):
    answer = ''
    for i in range(len(s)):
        if s[i]>1:
            answer +='{}'.format(i)*(s[i]//2)
    List = list(answer)
    List.reverse()
    answer = answer + "0" + "".join(List)
    return answer

def solution(food):
    answer = ''
    for i,n in enumerate(food[1:]):
        answer += str(i+1) * (n//2)
    return answer + "0" + answer[::-1]

print(solution([1, 3, 4, 6]))
#선수 두명이 먹는 음식의 종류와 양이 같아야 한다.
# 예를 들면 칼로리 적은 음식대로 1번음식 3개, 2번음식 4개 3번음식이 6개이고 물이 0이라면 각각 둘로나눠먹게되면  1223330221이된다.
# s             result
# [1, 3, 4, 6]	"1223330333221"
# [1, 7, 1, 2]	"111303111"