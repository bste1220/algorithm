import sys

sys.stdin = open('12.txt', 'r')


def rotate(arr): # 회전하는 함수
    N = len(arr)
    res = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            res[j][N - 1 - i] = arr[i][j]

    for i in range(N):
        for j in range(N):
            arr[i][j] = res[i][j] # arr을 값을 res로 설정

    return arr


T = int(input())
for tc in range(1, T + 1):
    N, C, X, Y, K, R = map(int, input().split())
    #  배열의크기 N, 회전각도 C, 시작위치 X,Y, 가로세로값 K,  출력행 R 입력받음
    nemo = [list(map(int, input().split())) for _ in range(N)]
    # 전체 배열을 이차원 리스트로 받는다.

    dist = (K - 1) // 2 # 배열 범위 정해줄려고 dist 정해줌
    arr = [[0] * K for _ in range(K)] # K X K 빈배열 만들어줌
    temp = [] # 새로운 배열 초기화
    try:
        for i in range(Y - dist, Y + dist + 1):
            for j in range(X - dist, X + dist + 1):
                temp.append(nemo[i][j]) #temp 배열에 추가
    except:
        print('#{} {}'.format(tc, -1))
        break

    for i in range(K):
        for j in range(K):
            arr[i][j] = temp[i * K + j]

    C = C // 90

    for i in range(C):
        rotate(arr) #

    r, c = 0, 0

    for i in range(Y - dist, Y + dist + 1):
        c = 0
        for j in range(X - dist, X + dist + 1):
            nemo[i][j] = arr[r][c]
            c += 1

        r += 1
    sol = 0
    for i in range(N):
        sol += nemo[R - 1][i] # R 의 행 합 출력

    print('#{} {}'.format(tc, sol))
