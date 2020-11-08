from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(1, 11):
    tc = input()
    miro = [list(map(int, input())) for _ in range(16)]
    visit = [[0] * 16 for _ in range(16)]
    res = 0
    q = deque()

    for i in range(16):
        for j in range(16):
            if miro[i][j] == 2:
                q.append((i, j))
                visit[i][j] = 1

    while q:
        x, y = q.popleft()

        if miro[x][y] == 3:
            res = 1
            break
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 16 and 0 <= ny < 16 and not visit[nx][ny]:
                if miro[nx][ny] != 1:
                    q.append((nx, ny))
                    visit[nx][ny] = 1

    print('#{} {}'.format(tc, res))
