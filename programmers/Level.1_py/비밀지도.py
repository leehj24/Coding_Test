def solution(n,arr1,arr2):
    answer = []
    for i in range(n):
        num = bin(arr1[i] | arr2[i])
        num = num[2:].zfill(n)
        num = num.replace('1', '#').replace('0', ' ')
        answer.append(num)
    return answer

#타풀이
solution = lambda n, arr1, arr2: ([''.join(map(lambda x: '#' if x=='1' else ' ', "{0:b}".format(row).zfill(n))) for row in (a|b for a, b in zip(arr1, arr2))])

# 배열 array를 이진법으로 하였을 때 0은 공백 1은 #으로 채웠을 경우 배열 2개를 합쳤을 때 둘중 하나라도 #있을시 채워놓는다 하였을 때 배열 합쳤을때의 결과를 return
# n    arr1                        arr2	                       result
# 5    [9, 20, 28, 18, 11]         [30, 1, 21, 17, 28]         ["#####","# # #", "### #", "# ##", "#####"]
# 6    [46, 33, 33 ,22, 31, 50]    [27 ,56, 19, 14, 14, 10]    ["######", "### #", "## ##", " #### ", " #####", "### # "]