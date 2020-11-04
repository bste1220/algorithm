def check(number, idx):
    global ans
    if number % 2 == 1:
        p = p1
    else:
        p = p2

    if p[idx] == 3:
        # 같은 카드가 3개 있으면 tri
        ans = number
    # 카드가 8보다 작으면 오른쪽으로 run 확인

    if idx < 8 and p[idx] and p[idx + 1] and p[idx + 2]:
        ans = number
    # 카드가 1보다 크면 왼쪽으로 run 확인
    if idx > 1 and p[idx] and p[idx - 1] and p[idx - 2]:
        ans = number
    #  양쪽으로 볼수 있다면 run 확인
    if 0 < idx < 9 and p[idx - 1] and p[idx] and p[idx + 1]:
        ans = number


T = int(input())
for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    ans = 0
    p1 = [0] * 10
    # 카드 받을 배열 만들어줌
    p2 = [0] * 10
    # 카드 받을 배열 만들어줌

    for i in range(len(card)):

        if i % 2 == 0:
            # 짝수면 p1 카드
            p1[card[i]] += 1

            check(1, card[i])
        else:
            # 아니면 p2 카드
            p2[card[i]] += 1

            check(2, card[i])
        if ans:
            break
    print('#{} {}'.format(tc, ans))
