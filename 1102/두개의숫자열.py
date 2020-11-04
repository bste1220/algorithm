def check(a, b):
    global maxV
    X = len(a)  # 작은길이
    Y = len(b)  # 긴길이
    for i in range(Y - X + 1):
        sum = 0

        for j in range(X):
            sum += a[j] * b[i + j]

        if maxV < sum:
            maxV = sum
    return maxV


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    maxV = -987654321
    res = 0
    if len(A) < len(B):
        res = check(A, B)
        # 체크함수에들어가고 리턴값을 res에 저장
    else:
        res = check(B, A)

    print('#{} {}'.format(tc, res))
