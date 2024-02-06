def solution(s):
    answer = []
    s_dict = dict()
    
    for i in range(len(s)):
        if s[i] not in s_dict:
            answer.append(-1)
        else:
            answer.append(i-s_dict[s[i]])
        s_dict[s[i]] = i
        
    return answer
    
def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] in s[0:i]:
            answer.append(i - s[0:i].rindex(s[i]))
        else:
            answer.append(-1)
    return answer

print(solution("banana"))
#s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 있다면 return
# s가 banana이면 마지막 a는 자신보다 두 칸, 네 칸 앞에 a가 있습니다. 이 중 가까운 것은 두 칸 앞이고, 이는 2로 표현합니다.

# banana    [-1, -1, -1, 2, 2, 2]
# foobar    [-1, -1, 1, -1, -1, -1]
