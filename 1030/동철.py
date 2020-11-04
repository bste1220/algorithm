def check(idx, end, res):
    global max_res
    if idx == end:
        if res > max_res:
            max_res = res
        return
    if res <= max_res:
        return
    for i in range(N):
        if not visit[i]:
            work = res * arr[idx][i] * (1/100)
            visit[i] = 1
            check(idx +1, end, work)
            visit[i] = 0
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    max_res = -987654321
    check(0, N, 1)

    print('#{} {:6f}'.format(tc, max_res*100))
