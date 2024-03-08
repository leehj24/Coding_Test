def check(s):
    answer = []
    s = s[2:-2]             #{{와 }} 제거
    s = s.split("},{")      #"},{"제거
    s.sort(key = len)       # 배열 크기 작은 순으로 배열
    for i in s:             # s= ['2', '2,1', '2,1,3', '2,1,3,4']
        ii = i.split(',')   # 배열 원소안에 , 제거
        for j in ii:
            if int(j) not in answer:
                answer.append(int(j))
    return answer

import re
 
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)
    for j in a:
        numbers = re.findall("\d+", j)
        for k in numbers:
            if int(k) not in answer:
                answer.append(int(k))
    return answer

print(check("{{2},{2,1},{2,1,3},{2,1,3,4}}"))


# 예를 들어 튜플이 (2, 1, 3, 4)인 경우 이는

# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# 와 같이 표현할 수 있습니다. 이때, 집합은 원소의 순서가 바뀌어도 상관없으므로

# {{2}, {2, 1}, {2, 1, 3}, {2, 1, 3, 4}}
# {{2, 1, 3, 4}, {2}, {2, 1, 3}, {2, 1}}
# {{1, 2, 3}, {2, 1}, {1, 2, 4, 3}, {2}}
# 는 모두 같은 튜플 (2, 1, 3, 4)를 나타냅니다.

# 특정 튜플을 표현하는 집합이 담긴 문자열 s가 매개변수로 주어질 때, s가 표현하는 튜플을 배열에 담아 return 하도록 solution 함수를 완성해주세요.