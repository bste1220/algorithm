T = int(input())
for _ in range(1, T + 1):
    s, score = 0, 0
    arr = input()
    for i in arr:
        if i == 'O':
            s += 1
            score += s
        else:
            s = 0

    print(score)
