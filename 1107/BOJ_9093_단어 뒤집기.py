N = int(input())
for _ in range(N):
    s = input()

    new = s[::-1]

    newlist = list(new.split(' '))

    # print(newlist)

    ss = []
    for i in range(N):
        while len(newlist):
            ss.append(newlist.pop())




    print(*ss)





