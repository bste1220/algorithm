from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]  # 상하좌우
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0] * M for _ in range(N)]
    Q = deque()
    Q.append((R, C))
    dist[R][C] = 1
    ans = 0
    while Q:
        x,y = Q.popleft()