def solution(str_list):
    for i,x in enumerate(str_list) :
        if x == "r" :
            return str_list[i+1:]
        elif x == "l" :
            return str_list[:i]
    return []
#str_list에서 "l"과 "r" 중 먼저 나오는 문자열이 "l"이라면 
# 해당 문자열을 기준으로 왼쪽에 있는 문자열들을 순서대로 담은 리스트를, 
# 먼저 나오는 문자열이 "r"이라면 해당 문자열을 기준으로 
# 오른쪽에 있는 문자열들을 순서대로 담은 리스트를 return

#str_list=["u","u","l","r"]	result=["u","u"]