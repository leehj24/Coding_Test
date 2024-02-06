def solution(arr, query):
    for i in range(len(query)):
        if i % 2 == 0:
            arr = arr[0:query[i]+1]
        else:
            arr = arr[query[i]:len(arr)]
    
    return arr

#짝수 인덱스에서는 arr에서 query[i]번 인덱스를 제외하고 
# 배열의 query[i]번 인덱스 뒷부분을 잘라서 버립니다.
#홀수 인덱스에서는 arr에서 query[i]번 인덱스는 제외하고 
# 배열의 query[i]번 인덱스 앞부분을 잘라서 버립니다.

#arr=[0,1,2,3,4,5] query= [4,1,2] result=[1,2,3]