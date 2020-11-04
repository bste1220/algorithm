def perm(n, k, m):
    if n == k:
        print(p)
    else:
        for i in range(m):
            if u[i] == 0:
                u[i] = 1
                p[n] = A[i]
                perm(n + 1, k, m)
                u[i] = 0


A = [1, 2, 3, 4, 5]
p = [0] * 3
u = [0] * 5
perm(0, 3, 5)
