def solution(myString, pat):
    answer=''
    for i in myString:
        if i =='A':
            answer +='B'
        elif i =='B':
            answer += 'A'
        else:
            answer +=i
    return int(pat in answer)
#"A"를 "B"로, "B"를 "A"로 바꾼 문자열의 연속하는 부분 문자열 중 
# pat이 있으면 1을 아니면 0을 return
#myString="ABBAA", pat= "AABB"	result =1