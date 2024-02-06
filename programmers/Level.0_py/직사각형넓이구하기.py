def solution(dots):
    a=max(dots)[0]-min(dots)[0]
    b=max(dots)[1]-min(dots)[1]
    return a*b

#dots=[[-1, -1], [1, 1], [1, -1], [-1, 1]] reuslt=4
#dots의 배열의 순서는 x,y좌표를 나열한 것이다. 네 좌표에 대한 직사각형 넓이를 구하여 return