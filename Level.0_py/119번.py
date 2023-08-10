def solution(myString):
    answer = ''
    for x in myString:
        if ord(x)<=ord("l"):
            answer+="l"
        else:
            answer+=x
    return answer
# 뮨저욜에서 l보다 앞선 문자는 전부 l로 변환
#myString="abcdeqrst" result="lllllqrst"