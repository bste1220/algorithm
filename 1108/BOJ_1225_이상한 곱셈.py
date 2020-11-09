import time
import sys

start_time = time.time()
N, M = input().split()
sum1 = 0
sum2 = 0
for i in N:
    sum1 += int(i)
for j in M:
    sum2 += int(j)


print(sum1 * sum2)

end_time = time.time()

print(end_time - start_time)
