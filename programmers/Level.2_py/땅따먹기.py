def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])
    return max(land[len(land) - 1])
print(solution([[5,6,4,2],[5,6,7,8],[4,3,2,1]]))

#땅land에서 가장 큰 수를 찾아 더해라
#같은 열이면 다른 열에서 가장 큰 수 를 찾아 더해야한다.