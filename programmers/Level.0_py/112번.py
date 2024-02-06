def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer+=i
    return answer


#str_list와 제외하려는 문자열 ex가 주어질 때, 
# str_list에서 ex를 포함한 문자열을 제외하고 만든 꼬리 문자열을 return

#str_list=["abc","def","ghi"] ex="ef" result="abcghi"