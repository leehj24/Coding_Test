def solution(common):
    if common[1]-common[0]==common[2]-common[1]:
        result= common[-1] + (common[2]-common[1])
    else:
        result= common[-1] *(common[2]//common[1])
    return  result

# 등차수열 혹은 등비수열 common이 매개변수로 주어질 때, 마지막 원소 다음으로 올 숫자를 return 
#   common      결과
#   [3,4,5]      6   
#   [2,4,8]      16