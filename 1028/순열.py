from itertools import permutations
from itertools import combinations


def perm(idx, k):  # idx : 숫자를 결정할 인덱스,(결정한개수)  k: 순열의길이
    if idx == k:
        print(arr)
        return

    for i in range(idx, k):
        arr[idx], arr[i] = arr[i], arr[idx]  # 현재 숫자 유지부터, 오른쪽 끝까지 교환
        perm(idx + 1, k)  # 다음 자리 결정하러 이동(n개 결정)
        arr[idx], arr[i] = arr[i], arr[idx]  # 교환전으로 복구


arr = [1, 2, 3]
perm(0, 3)
arr2 = [1, 2, 3, 4, 5]
new = list(permutations(arr2, 3))
new2 = list(combinations(arr2, 3))
print(new2)