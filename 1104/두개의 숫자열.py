def check(a, b):
    global maxV
    short = len(a)
    long = len(b)

    for i in range(long - short + 1):
        sum = 0
        for j in range(short):
            sum += a[j] * b[i + j]

        if maxV < sum:
            maxV = sum

    return maxV


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())  # A,B 배열 길이
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxV = -9876554321
    if N < M:
        res = check(A, B)
        # 여기선 A가 길이가 짧고 B의 길이가 길다.
    else:
        res = check(B, A)
        # B가 길이 짧고 A가 길이 길다.
    print('#{} {}'.format(tc, res))
