def solution(str_list):
    for i,x in enumerate(str_list) :
        if x == "r" :
            return str_list[i+1:]
        elif x == "l" :
            return str_list[:i]
    return []
