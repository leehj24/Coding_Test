# 플로이드-워셜 알고리즘을 이용한 경로 찾기
def floyd_warshall(graph, n):
    # 그래프 갱신: 모든 정점 쌍에 대해 경로 탐색
    for k in range(n):  # 중간 정점
        for i in range(n):  # 시작 정점
            for j in range(n):  # 도착 정점
                if graph[i][k] == 1 and graph[k][j] == 1:  # i -> k -> j 경로 확인
                    graph[i][j] = 1
    return graph

# 입력 처리
n = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(n)]  # 인접 행렬 입력

# 플로이드-워셜 알고리즘 실행
result = floyd_warshall(graph, n)

# 출력 결과
for row in result:
    print(" ".join(map(str, row)))
