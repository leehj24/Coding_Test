def solution(myString, pat):
    answer = 0
    string= myString.lower()
    low_pat=pat.lower()
    if low_pat in string:
        answer =1
    return answer

#myString 문자열에 pat문자열이 포함되면 1 // 대소문자는 판별하지 않음
#myString ="aBcDef" ,pat="Abc" ,result =1