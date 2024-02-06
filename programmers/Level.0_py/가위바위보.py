def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)
#또는
def solution(rsp):
    answer = ''
    for i in rsp :
        if i == '0' :
            answer += '5'
        elif i == '2' :
            answer += '0'
        else :
            answer += '2'
    return answer
#가위2 바위0 보5로 표현할때 rsp에 저장된 가위바위보를 모두 이기는 경우를 순서대로 나타난 문자열을 return
#rsp="205" result="052"