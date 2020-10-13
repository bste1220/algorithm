#10~ 99 사이의 난수 n 개 생성하기(13나오면 중단)
import random

n = int(input('난수의 갯수를 입력하세요.: '))

for _ in range(n):
    r = random.randint(10,99)
    print(r, end=" ")
    if r == 13:
        print('\n프로그램을 중단합니다.')
        break
else:
    print('\n난수생성을 종료합니다.')