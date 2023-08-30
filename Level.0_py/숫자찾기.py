def solution(num, k):
    answer = (str(num).find(str(k))+1)
    if answer == 0:
        answer = -1
    return answer

#또는
def solution(num, k):
    for i, n in enumerate(str(num)):
        if str(k) == n:
            return i + 1
    return -1

#num=65321 k=5 result=2
#num에 있는 k 숫자의 위치를 return