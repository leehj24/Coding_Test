def solution(order):
    answer = 0
    for i in str(order):
        if int(i)!=0 and int(i)%3==0:
            answer+=1
    return answer
#또는
def solution(order):
    answer = 0
    for i in str(order):
        if i in ["3","6","9"]:
            answer +=1
    return answer

#order=123456789 result=3
#order에 들어가있는 3,6,9 개수만큼 return