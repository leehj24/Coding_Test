def solution(emergency):
    return [sorted(emergency, reverse=True).index(e) + 1 for e in emergency]
#또는 
def solution(emergency):
    answer = []
    k=sorted(emergency,reverse=True)
    for i in emergency:
        answer.append(k.index(i)+1)
    return answer

#emergency=[3,5,8,9] result=[4,3,2,1] //emergency 원소의 큰 숫자부터 1부터 나열