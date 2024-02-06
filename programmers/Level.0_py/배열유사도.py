def solution(s1, s2):
    return len(set(s1)&set(s2))
#또는
def solution(s1, s2):
    answer = 0

    for i in s1:
        for j in s2:
            if i == j:
                answer += 1

    return answer
#배열안에 있는 문자열이 같은 수만큼 return
# s1=["a","b","c"] ,s2=["com","b","c","d","p"] result=2