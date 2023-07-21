def solution(n, slicer, num_list):
    answer = []
    if n==1:
        answer=num_list[0:slicer[1]+1]
    elif n==2:
        answer=num_list[slicer[0]::]
    elif n==3:
        answer=num_list[slicer[0]:slicer[1]+1]
    else:
        answer=num_list[slicer[0]:slicer[1]+1:slicer[2]]
        print(slicer[1])
    return answer

#또는
def solution(n, slicer, num_list):
    answer = []
    a, b, c = slicer
    
    if n == 1:
        answer = num_list[0:b+1]
    elif n == 2:
        answer = num_list[a:]
    elif n == 3:
        answer = num_list[a:b+1]
    elif n == 4:
        answer = [num_list[i] for i in range(a, b + 1, c)]
    
    return answer