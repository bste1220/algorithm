H, M = map(int, input().split())

if M >= 45:
    print('{} {}'.format(H, M - 45))


elif H == 0:
    print('{} {}'.format(23, M + 15))
else:
    print('{} {}'.format(H - 1, M + 15))
