def solution(array, n):
    return array.count(n)
#또는 
def solution(array, n):
    answer = 0
    for i in array:
        if i ==n:
            answer +=1
    return answer

#정수 배열에 n이 들어간 숫자의 개수를 return
# array=[1,1,2,3,4,5] , n=1 , result=2