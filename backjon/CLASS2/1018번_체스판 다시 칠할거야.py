def count_repaints(board, start_row, start_col):
    # 두 가지 경우의 체스판 패턴
    pattern1 = ["WBWBWBWB", "BWBWBWBW"] * 4
    pattern2 = ["BWBWBWBW", "WBWBWBWB"] * 4
    
    repaint1, repaint2 = 0, 0
    for i in range(8):
        for j in range(8):
            if board[start_row + i][start_col + j] != pattern1[i][j]:
                repaint1 += 1
            if board[start_row + i][start_col + j] != pattern2[i][j]:
                repaint2 += 1
    
    return min(repaint1, repaint2)

def min_repaints_to_chessboard(N, M, board):
    min_repaints = float('inf')
    for i in range(N - 7):
        for j in range(M - 7):
            min_repaints = min(min_repaints, count_repaints(board, i, j))
    return min_repaints

# 입력 받기
N, M = map(int, input().split())
board = [input().strip() for _ in range(N)]

# 결과 출력
print(min_repaints_to_chessboard(N, M, board))
