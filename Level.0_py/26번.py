def solution(num_list):
    a=num_list[-1]
    b=num_list[-2]
    if a>b:
        num_list.append(a-b)
    else: 
        num_list.append(2*a)
    return num_list
#num_list = [2,1,5] result=[2,1,6,5] 
#num_list = [2,5,3] result=[2,5,3,6]
#마지막 수와 뒤에서 두번째수의 차이를 보고 리스트 추가
solution()