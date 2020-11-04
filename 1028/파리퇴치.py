T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            fly = 0
            for x in range(M):
                for y in range(M):
                    fly += arr[i+x][j+y]

            if max < fly:
                max = fly

    print('#{} {}'.format(tc,max))
