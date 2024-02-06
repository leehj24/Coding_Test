def solution(score):
    result=[]
    aver=[]
    for i in score:
        aver.append(sum(i)//2)
    aver_Sort = sorted(aver,reverse=True)
    for i in aver:
        result.append(aver_Sort.index(i)+1)
    return  result

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]

#    score                          result
# [[80, 70], [90, 50],           [1, 2, 4, 3]
# [40, 70], [50, 80]]            

# [[80, 70], [70, 80],           [4, 4, 6, 2, 2, 1, 7]
# [30, 50], [90, 100], 
# [100, 90], [100, 100], 
# [10, 30]]	