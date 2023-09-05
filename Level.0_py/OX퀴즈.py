def solution(quiz):
    answer = []
    for i in quiz:
        print(i.split('=')) # ["1+2","3"]으로 출력
        if eval(i.split('=')[0]) == int(i.split('=')[1]):
            answer.append('O')
        else:
            answer.append('X')
    return answer
# quiz["1+2=3", "3-4=8"] result=["O","X"]
# quiz에 문자열을 계산한 값이 맞으면 O 틀리면 X를 순서대로 담은 배열을 return