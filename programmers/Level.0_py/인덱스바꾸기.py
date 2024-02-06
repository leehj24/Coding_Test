def solution(my_string, num1, num2):
    answer=''
    my_string = list(my_string)
    my_string[num1], my_string[num2] = my_string[num2], my_string[num1]
    return answer.join(my_string)
#또는
def solution(my_string, num1, num2):
    return my_string[:num1]+my_string[num2]+my_string[num1+1:num2]+my_string[num1]+my_string[num2+1:]

# my_string의 문자열에서 인덱스 num1과 num2를 바꾼후 return
# my_string="hello" num1=1 num2=2 result="hlelo"