dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    INF = int(1e9)
    distance = [INF] * (N + 1)

    print(distance)
