def solution(myString):
    a=[]
    for x in myString.split('x'):
        if x: a.append(x)
    return sorted(a)

#문자열 'x'를 제외한 문자를 알파벳 순으로 배열
# myString="dxccxbbbxaaaa"	result=["aaaa","bbb","cc","d"]