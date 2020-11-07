def _sum(n):
    res = 0
    for i in n:
        res += i

    return res

N = int(input())
arr = [int(i) for i in range(N + 1)]


print(_sum(arr))