def solution(my_string):
    return sorted([int(c) for c in my_string if c.isdigit()])
#또는
def solution(my_string):
    answer = []
    for i in my_string:
        try:
            answer.append(int(i))
        except:
            continue
    answer.sort()
    return answer
#문자열 my_String에 숫자를 오름차순으로 배열후 return
#my_string="hi1254mts" result=[1,2,3,4,5]