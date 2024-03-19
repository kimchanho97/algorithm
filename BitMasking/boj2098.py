import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * (1 << n) for _ in range(n)]

# 시작점: 0
# 현재 위치: cur_town
# 경로: visited
# 방문하지 않은 마을들을 순회한 뒤, 시작점까지 돌아오는 최소거리
def tsp(cur_town, visited):
    # 모두 방문한 경우
    if visited == (1 << n) - 1:
        if graph[cur_town][0] != 0:  # 시작점으로 돌아가는 경로가 존재할 경우
            dp[cur_town][visited] = graph[cur_town][0]
        else:
            dp[cur_town][visited] = float('inf')
        return dp[cur_town][visited]

    if dp[cur_town][visited] != 0:
        return dp[cur_town][visited]

    # temp = f'{visited:0{n}b}'  # bit-string

    cost = float('inf')
    for i in range(1, n):
        # 방문하지 않은 곳의 경로가 존재할 경우
        if visited & (1 << i) == 0 and graph[cur_town][i] != 0:
            cost = min(tsp(i, visited | (1 << i)) + graph[cur_town][i], cost)
    dp[cur_town][visited] = cost

    return dp[cur_town][visited]

print(tsp(0, 1))