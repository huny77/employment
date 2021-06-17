import sys

sys.stdin = open('input.txt')


def find(node: int) -> int:
    if data[node] != node:
        data[node] = find(data[node])
    return data[node]


def union(a: int, b: int) -> None:
    root1 = find(a)
    root2 = find(b)

    if root1 == root2:
        return

    if rank[root1] > rank[root2]:
        root1, root2 = root2, root1

    data[root1] = root2

    if rank[root1] == rank[root2]:
        rank[root2] += 1


n = int(input())
node = []
for i in range(n):
    x, y, z = map(int, input().split())
    node.append((x, y, z, i))

edges = []
for i in range(3):
    node.sort(key=lambda x: x[i])
    for j in range(1, n):
        edges.append((abs(node[j - 1][i] - node[j][i]), node[j - 1][3], node[j][3]))

data = {key: key for key in range(n + 1)}
rank = {key: 1 for key in range(n + 1)}

total = 0
edges.sort()

for i in range(len(edges)):
    weight, a, b = edges[i]
    if find(a) != find(b):
        union(a, b)
        total += weight
print(total)
