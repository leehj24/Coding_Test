from itertools import combinations
def solution(numbers):
    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))


def solution(numbers): 
    return sorted({numbers[i] + numbers[j] for i in range(len(numbers)) for j in range(len(numbers)) if i>j})

def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

def solution(number):
    answer=[] ; array =[]
    for i in range(len(number)):
        for j in range(i+1, len(number)):
            print(number[i], number[j])
            answer.append(number[i]+number[j])
    answer.sort()
    
    for k in range(len(answer)+1):
        answer.append("")
        if answer[k]==answer[k+1]:
            pass
        else:
            array.append(answer[k])
    return array

#numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return

#numbers	    result
#[2,1,3,4,1]	[2,3,4,5,6,7]
#[5,0,2,7]	    [2,5,7,9,12]

# 2+1=3,    2+3=5,  2+4=6,  2+1=3,  1+3=4,....