from collections import deque

tunnel = {
    0: (),
    1: ((1, 0), (0, 1), (-1, 0), (0, -1)),
    2: ((1, 0), (-1, 0)),
    3: ((0, 1), (0, -1)),
    4: ((-1, 0), (0, 1)),
    5: ((1, 0), (0, 1)),
    6: ((1, 0), (0, -1)),
    7: ((-1, 0), (0, -1))
}

T = int(input())
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    q = deque([(R, C)])
    visit = [[0] * M for _ in range(N)]
    visit[R][C] = 1
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in tunnel[arr[x][y]]:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < N or not 0 <= ny < M:
                continue
            if (-dx, -dy) in tunnel[arr[nx][ny]]:
                if not visit[nx][ny] and arr[nx][ny]:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    if visit[nx][ny] <= L:
                        cnt += 1
    print('#{} {}'.format(tc, cnt))
