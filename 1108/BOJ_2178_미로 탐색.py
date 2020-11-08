import time
start_time = time.time()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]
dist = [[0] * M for _ in range(N)]

stack = []
stack.append((0, 0))
dist[0][0] = 1

while stack:
    x, y = stack.pop()

    if x == N - 1 and y == M - 1:
        print(dist[x][y])

        break

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]

        if 0 <= nx < N and 0 <= ny < M and not dist[nx][ny]:
            if miro[nx][ny] == 1:
                dist[nx][ny] = dist[x][y] + 1
                stack.append((nx, ny))
end_time = time.time()

print(end_time-start_time)
