for tc in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        big = box.index(max(box))
        small = box.index(min(box))

        box[big] -= 1
        box[small] += 1

    res = box[big] - box[small]


    print('#{} {}'.format(tc, res))