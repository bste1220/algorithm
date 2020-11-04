S = input()
change_0, change_1 = 0, 0
for i in range(len(S)):
    if S[i] != S[i - 1]:
        if S[i - 1] == '0':
            change_1 += 1

        else:
            change_0 += 1

print(min(change_0, change_1))
