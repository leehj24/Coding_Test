def solution(num_list):
    answer = 0
    for i in num_list:
        count = 0
        while i !=1:
            count+=1
            if i%2==0:
                i =i/2
            else:
                i =(i-1)/2
        answer +=count
    return answer
#num_list에 있는 수를 1이 될때까지 2로 나눈다. 연산 횟수를 추출
#num_list=[3,10,11] result= 7