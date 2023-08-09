def solution(num_list):
    a=""#홀수
    b=""#짝수
    for i in num_list:
        if i%2!=0:
            a+=str(i)
        else:
            b+=str(i)
    return int(a)+int(b)

# numlist= [3,4,5,2,1] result= 393 
# numlist= [5,7,8,3] result= 581
# 홀수인 341 과 짝수인 42를 더하여 393이 나옴
# 홀수인 523과 짝수인 8을 더하여 581이 나옴