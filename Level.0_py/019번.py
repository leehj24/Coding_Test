#flag가 true면 더하기, flase면 빼기를 한다
def solution(a, b, flag):
    if flag:
        answer = a +b
    else:
        answer = a-b
    return answer