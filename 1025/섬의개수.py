def DFS(x, y):
    visit[x][y] = 1

    for d in range(8):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
            if arr[nx][ny]:
                DFS(nx, ny)


dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if not visit[r][c] and arr[r][c]:
                cnt += 1
                DFS(r, c)

    print(cnt)