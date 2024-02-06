def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))
# "5-8" -> "5+(-8)" reuslt=-3

def solution(my_string):
    return eval(my_string)
# 문자열에 있는 숫자를 계산하여 return
# my_string"= "1+2" result=3 //eval은 문자열 식 값을 반환