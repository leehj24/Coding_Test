def solution(my_string):
    answer = 0
    for x in my_string:
        if x.isdigit():
            answer+=int(x)
    return answer
#또는
def solution(my_string):
    answer = 0
    for c in my_string:
        if c.isnumeric():
            answer += int(c)
    return answer
#또는
def solution(my_string):
    answer = 0
    for i in my_string:
        if ord(i)<65: #아스키코드로 변한
            answer +=int(i)
    return answer

 #문자열에 숫자만 골라 더해 return
 # my_string="AaBc12j3dfg4of5" result=10