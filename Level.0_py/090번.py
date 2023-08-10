def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i =="m":
            answer += "rn"
        else:
            answer +=i
    return answer

# rny_string의 모든 'm'을 "rn"으로 바꾼 문자열을 return
#rny_string="masterpiece"	result="rnasterpiece"