def solution(myString, pat):
    cnt = 0
    for i in range(len(myString)-len(pat)+1):
        if myString[i:i+len(pat)] == pat:
            cnt += 1

    return cnt

#문자열 myString과 pat이 주어짐, myString에서 pat이 등장하는 횟수를 return 함
#myString='banana' pat='ana' result2