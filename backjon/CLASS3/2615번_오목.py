def check_winner(board):
    # 탐색 방향: 가로(→), 세로(↓), 우하 대각선(↘), 우상 대각선(↗)
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]
    
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                stone = board[x][y]
                
                for dx, dy in directions:
                    count = 1
                    nx, ny = x + dx, y + dy
                    
                    while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == stone:
                        count += 1
                        if count == 5:
                            # 6목 방지 (앞뒤로 같은 색이 있는 경우)
                            if 0 <= x - dx < 19 and 0 <= y - dy < 19 and board[x - dx][y - dy] == stone:
                                break
                            if 0 <= nx + dx < 19 and 0 <= ny + dy < 19 and board[nx + dx][ny + dy] == stone:
                                break
                            return stone, x + 1, y + 1  # 1-based index 반환
                        
                        nx += dx
                        ny += dy
    
    return 0, None, None

# 입력 받기
board = [list(map(int, input().split())) for _ in range(19)]

# 승자 판별
winner, x, y = check_winner(board)

# 결과 출력
if winner:
    print(winner)
    print(x, y)
else:
    print(0)
