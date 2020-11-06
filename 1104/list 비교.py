set1 = [1, 4, 6, 7, 8, 9]
set2 = [4, 8, 1, 9]

res = []
#
# for s1 in set1:
#     if s1 in set2:
#         res.append(s1)

for s1 in set1:
    for s2 in set2:
        if s1 == s2:
            res.append(s1)
print(res)
