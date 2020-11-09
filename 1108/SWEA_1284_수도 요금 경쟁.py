T = int(input())
for tc in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if R > W:
        B = Q



    else:

        B = Q + ((W - R) * S)

    print('#{} {}'.format(tc, min(A, B)))
