def solution(box, n):
    answer = 1
    for i in box:
        a = i//n
        answer *= a
    return answer
#또는
def solution(box, n):
    return (int(box[0] //n) * int(box[1] // n) * int(box[2] //n))

#직육면체 박스안에 주사위가 들어가는 개수를 return
#box의 배열은 순서대로 가로세로높이이고 n은 주사위 모서리의 길이
#box[10,8,7] n=3 result=12