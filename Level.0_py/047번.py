def solution(my_string, is_prefix):
    if is_prefix == my_string[:len(is_prefix)]:
        return 1
    else:
        return 0
#my_string="banana" is_prefix="ban" result =1
#is_prefix이 my_string의 문자열 접두사 이면 1을 출력