def solution(s):
    p = 0 ; y = 0
    for i in s.lower():
        if i == "p":
            p +=1
        elif i =="y":
            y +=1
    if p==y:
        answer = True
    else:
        answer = False
    return answer


def solution(s):
    return s.lower().count('p')==s.loswer.count('y')

#대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 
#   s	    answer
#'pPoooyY'	True
#'Pyy'	    False


