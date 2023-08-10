def solution(n_str):
    return str(int(n_str))
#또는 
def solution(n_str):
    return n_str.lstrip("0")
#문자열 n_str에 앞에있는 0을 제외한 숫자를 return
#n_str="0010" result="10"