def solution(my_string, is_suffix):
    k=[]
    for i in range(len(my_string)):
        k.append(my_string[i::])
    if is_suffix in k:
        answer =1
    else:
        answer =0
    return answer
# is_suffix 이 my_string 의 접미사인지 확인
# my_string="banana" , is_suffix="ana" , result = 1