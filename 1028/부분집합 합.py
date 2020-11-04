arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
cnt = 0
for i in range(1 << N):
    SUM = 0
    sub = []
    for j in range(N):
        if i & (1 << j):
            sub.append(arr[j])
            SUM += int(arr[j])

    if SUM == 0:
        cnt += 1
        print(sub)

