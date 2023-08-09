#문자열 섞기 <입력: aaaa bbbb 일경우> <출력: abababab>
def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer
solution()