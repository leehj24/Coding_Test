def solution(my_string):
    answer = []
    for i in range(0,len(my_string)):
        answer.append(my_string[i:])
    return sorted(answer)
#문자열의 접미사 오름차순으로 추출
# my_string= "banana", "result = ["a","ana","anana","banana","na","nana"]