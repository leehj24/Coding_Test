def solution(array):
    return str(array).count('7')
#또는
def solution(array):
    answer = ''
    for i in array:
        answer +=str(i)
    return answer.count('7')
# 문자열 array의 원소에서 숫자 7의 개수를 return
# array =[7,17,77] , result=4