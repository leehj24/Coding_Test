def solution(my_string, s, e):
    answer = my_string[0:s]+my_string[s:e+1][::-1]+my_string[e+1::]
    return answer
#my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성
# my_string= "Progra21Sremm3" ,s=6,e=12, result= "ProgrammerS123"