def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a' or i == 'A':
            i = i.upper()
        else:
            i = i.lower()
        answer += i
    return answer
#myString 문자열에 a문자만 대문자이고 타 문자는 소문자로 변경
#myString="ArraySpRing" result="ArrAyspring" 