def solution(m, n, board):
    board = [list(row) for row in board]  # 문자열을 리스트로 변환
    answer = 0

    while True:
        remove = set()
        # 2x2 블록 탐지
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != ' ' and board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1]:
                    remove.update([(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)])

        if not remove:  # 제거할 블록이 없으면 종료
            break

        # 블록 제거
        for i, j in remove:
            board[i][j] = ' '
        answer += len(remove)

        # 블록 아래로 떨어뜨리기
        for j in range(n):
            empty = [i for i in range(m) if board[i][j] == ' ']
            filled = [board[i][j] for i in range(m) if board[i][j] != ' ']
            for i in range(m):
                board[i][j] = ' ' if i < len(empty) else filled[i - len(empty)]

    return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))  # 14

#이 코드는 2x2 블록을 탐지하고 제거한 후, 빈 공간을 채우는 과정을 반복합니다. 
# set을 사용해 중복 제거를 방지하며, 
# 블록이 더 이상 제거되지 않을 때 종료합니다.

# 입출력 예제 1의 경우, 첫 번째에는 A 블록 6개가 지워지고, 
# 두 번째에는 B 블록 4개와 C 블록 4개가 지워져, 모두 14개의 블록이 지워진다.
