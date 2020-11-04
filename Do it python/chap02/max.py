#시퀀스 원소의 최대값 출력하기

from typing import Any, Sequence

def max_of(a:Sequence) -> Any:
    """시퀀스형 a 원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':
    print('배열의 최대값을 구합니다.')
    num = int(input('원소 수를 입력하세요.:'))
    x = [None] * num

    for i in range(num):

        print('최대값은 {}입니다'.format(max_of(x)))
