def coke(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
    
def solution(X, Y):
    xList = list(X.count(str(x)) for x in range(10))
    yList = list(Y.count(str(y)) for y in range(10))
    answer = ""
    for i in range(9, -1, -1):
        answer += str(i) * min(xList[i], yList[i])

    if answer == "":
        return "-1"
    elif answer[0] == "0" and answer[len(answer) - 1] == "0":
        return "0"
    else:
        return answer
    
print(coke("5525","51255"))
#문자열 X,Y곂치는 숫자를 나열하여 제일 높은 수로 만들어 return 없으면 -1을 return
#X        Y	    result
#"100"	"2345"	"-1"
#"5525" "51255" "5552"