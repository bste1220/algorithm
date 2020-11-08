A = int(input())
B = int(input())

strB = str(B)
NEW = []
for i in strB:
    NEW.append(int(i) * A)
NEW = NEW[::-1]
res = 0
for x in range(len(NEW)):
    res += NEW[x] * (10 ** x)


NEW.append(res)

for j in NEW:
    print(j)