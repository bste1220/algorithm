N = int(input())
switch = list(map(int, input().split()))
student = int(input())
on_off = {1: 0, 0: 1}
# 스위치가 1일때 0 으로 변경, 0일때 1으로 변경하는 딕셔너리 만듬
for _ in range(student):
    gender, num = map(int, input().split())
    # 남자일 경우
    if gender == 1:
        i = num
        while i - 1 < N:
            switch[i - 1] = on_off[switch[i - 1]]
            i += num

    # 여자일 경우
    else:
        i, j = num - 2, num
        switch[num - 1] = on_off[switch[num - 1]]
        while i >= 0 and j < N:
            if switch[i] == switch[j]:
                switch[i], switch[j] = on_off[switch[i]], on_off[switch[j]]
            else:
                break
            i -= 1
            j += 1

for i in range(0, N, 20):
    print(*switch[i:i + 20])
