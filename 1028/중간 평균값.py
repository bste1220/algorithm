T = int(input())

for tc in range(1, T + 1):
    arr = list(map(int, input().split()))

    new_list = sorted(arr)
    res = 0
    for i in range(1, 9):
        res += new_list[i]

    arr = res // 8


    print('#{} {}'.format(tc, arr))
