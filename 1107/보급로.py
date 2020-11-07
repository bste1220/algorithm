from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dijkstra(q):
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if distance[nx][ny] > distance[x][y] + arr[nx][ny]:
                    distance[nx][ny] = distance[x][y] + arr[nx][ny]
                    q.append((nx, ny))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    INF = int(1e9)
    distance = [[INF for _ in range(N)] for _ in range(N)]

    distance[0][0] = 0
    q = deque()
    q.append((0, 0))
    dijkstra(q)

    print('#{} {}'.format(tc, distance[N - 1][N - 1]))
