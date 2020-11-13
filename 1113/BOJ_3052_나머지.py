arr = []
for _ in range(10):
    num = int(input())
    arr.append(num)

set1 = set()
for i in arr:
    set1.add(i % 42)

print(len(set1))