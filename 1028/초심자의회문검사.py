T = int(input())
for tc in range(1, T + 1):
    str1 = list(input())
    # print(s)
    str2 = str1[::-1]

    if str1 == str2:
        print('#{} {}'.format(tc, 1))
    else:
        print('#{} {}'.format(tc, 0))
