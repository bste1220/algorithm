def perm(n, k, m):  # 숫자를 결정할 자리인덱스, k : 순열의 길이 , m : 주어진 숫자의 개수
    if n == k:
        print(A[0:k])
    else:
        for i in range(n, m): # n 번과 바꿀 위치
            A[n], A[i] = A[i], A[n]
            perm(n+1, k, m)
            A[n], A[i] = A[i], A[n]


A = [1, 2, 3, 4, 5]
perm(0, 3, 5)
