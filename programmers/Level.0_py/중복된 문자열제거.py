def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in answer:
            answer+=i
    return answer
#my_string =''hellow world" result="hellow rd"
#문자열 my_string에서 중복되는 문자열을 제거하여 다시 return