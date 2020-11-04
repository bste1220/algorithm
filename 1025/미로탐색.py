dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

N, M = map(int, input().split())

arr = [list(map(int, input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

q = [(0, 0)]
dist[0][0] = 1

while q:
    x, y = q.pop(0)

    if x == N - 1 and y == M - 1:
        print(dist[x][y])

        break
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1 and not dist[nx][ny]:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))
