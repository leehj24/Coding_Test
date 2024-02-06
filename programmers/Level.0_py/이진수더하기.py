def solution(bin1, bin2):
    answer = ''
    a=int(bin1,2)
    b=int(bin2,2)
    answer=str(bin(a+b))
    return answer[2::]
#또는
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

#bin1='101' , bin2='100' result='1001'
#이진수 bin1과 bin2를 더하여 return