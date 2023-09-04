def solution(my_string):
    answer = 0
    temp = ''
    for i in my_string:
        if i.isdigit():
            temp += i
        else:
            if temp:
                answer += int(temp)
                temp = ''
    if temp:
        answer += int(temp)
    return answer

#또는 
import re
def solution(my_string):
    num = re.findall(r'\d+', my_string)
    num = list(map(int, num))
    return sum(num)

 #문자열에 숫자만 골라 더해 return
 # my_string="AaBc12j3dfg4of5" result=24 //12+3+4+5