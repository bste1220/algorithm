# from itertools import combinations
# 3C2
arr = [3, 2, 8, 8, 8]
N = len(arr);
cnt = 2

ans = 0


def backtrack(k):
    if k == cnt:
        num = int(''.join(map(str, arr)))
        if ans < num:
            ans = num ; print(ans)
    else
        for i in range(N - 1):
            for j in range(i + 1, N):
                arr[i], arr[j] = arr[j], arr[i]
                backtrack(k + 1)

                # 재귀 호출
                arr[i], arr[j] = arr[j], arr[i]
backtrack(0)
print()
# T = int(input())
# for tc in range(1. T+1):
#     number, change = map(int, input().split())
#     N = len(change)
#     for i in range(N):
