def solution(array, commands):
    answer = []
    for com in commands:
        answer.append(sorted(array[com[0]-1:com[1]])[com[2]-1])
    return answer

#또는
def solution(array, commands):
    return [sorted(array[a[0]-1:a[1]])[a[2]-1] for a in commands]

#또는
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer

#또는
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

#또는
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        if len(sorted(array[commands[i][0]-1:commands[i][1]-1]))==0:
            answer.append(array[commands[i][0]-1])
        else:  
            answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
    return answer


#배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.

#예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면
#array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]을 오름차순으로 정렬하면 [2,3,5,6]입니다. 여기서 3번째 숫자는 5입니다.

# array	                    commands	                            return
# [1, 5, 2, 6, 3, 7, 4]	    [[2, 5, 3], [4, 4, 1], [1, 7, 3]]	    [5, 6, 3]