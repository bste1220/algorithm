A, B = input().split()

r_A = A[::-1]
r_B = B[::-1]

if int(r_A) < int(r_B):
    print(r_B)
else:
    print(r_A)