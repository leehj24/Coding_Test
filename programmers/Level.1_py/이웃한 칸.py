def coke(board, h, w):
    n = len(board)
    answer = 0
    dh,dw=[1,-1,0,0],[0,0,1,-1]
    for i,j  in zip(dh,dw):
        nh,nw = i+h, j+w
        if nh<0 or nh>=n or nw<0 or nw>=n:
            continue
        if board[h][w]==board[nh][nw]:
            answer +=1
    return answer
            
def solution(board, h, w):
    n = len(board)
    count = 0
    dh,dw = [0, 1, -1, 0], [1, 0, 0, -1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n  and  0 <= w_check < n and board[h][w] == board[h_check][w_check]:
            count += 1

    return count

def solution(board, h, w):
    n = len(board)
    count = 0
    dh,dw = [0, 1, -1, 0], [1, 0, 0, -1]
    
    for i in range(4):
        h_check, w_check = h + dh[i], w + dw[i]
        if 0 <= h_check < n  and  0 <= w_check < n and board[h][w] == board[h_check][w_check]:
            count += 1

    return count

def solution(board, h, w):
    count = 0
    key = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    
    return count


print(coke([["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]],1,1))

#board[h][w]위아래 우좌에 같은 색있는 개수를 return