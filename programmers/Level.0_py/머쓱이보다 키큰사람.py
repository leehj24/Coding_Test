def solution(array, height):
    return sum(1 for a in array if a > height)
#또는
def solution(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer +=1
    return answer
# height보다 큰 키인 사람의 수를 return
# array=[149,180,192,170] , height=167 , result=3