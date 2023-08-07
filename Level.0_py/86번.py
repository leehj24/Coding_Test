def solution(myString):
    answer = []
    tmp = myString.split('x')
    return [len(i) for i in tmp]

#문자열 "x"사이에 있는 개수를 배열로 추출
#myString="oxooxoxxox"	result=[1, 2, 1, 0, 1, 0]