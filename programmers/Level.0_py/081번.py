def solution(myString, pat):
    return myString[:len(myString) - myString[::-1].index(pat[::-1])]

#myString의 부분 문자열중 pat로 끝나는 가장 긴 부분 문자열을 찾아서 return
# myString="AbCdEFG"	pat="dE"	result="AbCdE"