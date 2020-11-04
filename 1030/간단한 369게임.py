N = int(input())

arr = [str(i) for i in range(1, N + 1)]

for x in range(len(arr)):
    temp = ""
    for y in arr[x]:
        if y in ('3', '6', '9'):
            temp += '-'
            arr[x] = temp

print(*arr)
