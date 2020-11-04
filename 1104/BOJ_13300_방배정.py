N, K = map(int, input().split())
arr = [[0] * 7 for _ in range(2)]
# 일단 학생수
room = 0
for _ in range(N):
    gender, grade = map(int, input().split())

    arr[gender][grade] += 1

for i in range(2):
    for j in range(1, 7):
        room += arr[i][j] // K
        if arr[i][j] % K:
            room += 1

print(room)
