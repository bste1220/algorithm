import sys

sys.stdin = open('1.txt', 'r')

S = input().strip()
tmp = ''
ans = ''
flag = False

for i in S:
    if i == ' ':
        ans += tmp[::-1] + i
        tmp = ''
    elif i == '<':
        flag = True
        ans += tmp[::-1] + i
        tmp = ''
    elif i == '>':
        flag = False
        ans += i
    elif flag:
        ans += i
    else:
        tmp += i

ans += tmp[::-1]

print(ans)
