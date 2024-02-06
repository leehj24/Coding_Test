def solution(my_string):
    return ''.join(sorted(my_string.lower()))

#또는 

def solution(my_string):
    answer = ''
    k=sorted(my_string.lower())
    for i in k:
        answer +=i
    return answer

#my_string ="Bcad" result="abcd"
#my_string에 있는 문자열을 소문자로 변환한 후 오름차순으로 정렬한 후 return