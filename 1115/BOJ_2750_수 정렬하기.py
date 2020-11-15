N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

sort_arr = sorted(arr)

for i in sort_arr:
    print(i)