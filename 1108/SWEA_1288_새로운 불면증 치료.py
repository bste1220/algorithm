T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    check = [False] * 10
    cnt = 0
    j = 1

    while cnt != 10:
        sleep = str(N * j)
        for i in sleep:
            if check[int(i)] == False:
                check[int(i)] = True
                cnt += 1
        j += 1

    print('#{} {}'.format(tc, N * (j - 1)))
