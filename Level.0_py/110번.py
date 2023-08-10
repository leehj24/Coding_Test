def solution(my_string, target):
    if target in my_string:
        return 1
    else:
        return 0

#target이 문자열 my_string의 부분 문자열이라면 1을, 아니라면 0을 return
#my_string="banana", target="ana" result=1