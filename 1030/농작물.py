T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    # print(arr)
    mid = N // 2
    # 가운데 값 저장
    res = 0
    for i in range(N):
        # 증가하는
        if i <= mid:
            for j in range(mid - i, (mid + i) + 1):
                res += arr[i][j]
        #감소하는
        else:
            for j in range((i - mid), N - (i - mid)):
                res += arr[i][j]
    print('#{} {}'.format(tc, res))
