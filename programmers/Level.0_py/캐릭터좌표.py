def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    for key in keyinput:
        if key == 'left' and x > board[0] // -2 + 1:
            x -= 1
        if key == 'right' and x < board[0] // 2:
            x += 1
        if key == 'up' and y < board[1] // 2:
            y += 1
        if key == 'down' and y > board[1] // -2 + 1:
            y -= 1
    answer.append(x)
    answer.append(y)
    return answer

def solution(keyinput, board):
    col = board[0]
    row = board[1]
    result = [0, 0]
    for i in keyinput:
        if i == "left" and result[0]-1 >= -(col // 2):
            result[0] -= 1
        elif i == "right" and result[0]+1 <= (col // 2):
            result[0] += 1
        elif i == "up" and result[1]+1 <= (row // 2):
            result[1] += 1
        elif i == "down" and result[1]-1 >= -(row // 2):
            result[1] -= 1
    return result

# keyinput=["left", "right", "up", "right", "right"], board=[11, 11], result=[2, 1]
# up을 누른다면 캐릭터의 좌표는 [0, 1], down을 누른다면 [0, -1], left를 누른다면 [-1, 0], right를 누른다면 [1, 0]입니다. 
# 머쓱이가 입력한 방향키의 배열 keyinput와 맵의 크기 board이 매개변수로 주어집니다. 
# 캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 캐릭터의 좌표 [x, y]를 return