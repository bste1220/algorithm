def preorder(node):

    if node:
        print(node, end=" ")

        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):

   if node:
       inorder(tree[node][0])
       print(node, end=" ")
       inorder(tree[node][1])

def postorder(node):

    if node:
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end=" ")


V = int(input())
E = V - 1
tree = [[0] * 3 for _ in range(V + 1)]
temp = list(map(int, input().split()))


for i in range(E):
    p, c = temp[i * 2], temp[i * 2 + 1]
    if tree[p][0] == 0:
        tree[p][0] = c
    else:
        tree[p][1] = c
    tree[c][2] = p



preorder(1)
print()
inorder(1)
print()
postorder(1)