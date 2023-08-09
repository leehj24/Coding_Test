def solution(my_string, alp):
    answer = ""
    for i in my_string:
        if i ==alp:
            answer +=i.upper()
        else:
            answer +=i
    return answer
#alp의 문자열 만 mystring에 대문자로 변경
#mystring="mystar" alp="y" result="mYstar"