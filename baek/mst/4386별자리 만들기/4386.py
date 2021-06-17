import sys
from itertools import combinations

sys.stdin = open('input.txt')

n = int(input())
node = []
for i in range(n):
    a, b = map(float, input().split())
    node.append([i, a, b])
edges = []

for a, b in combinations(node, 2):
    i1, x1, y1 = a
    i2, x2, y2 = b
    distance = round((abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5, 2)
    edges.append([a[0], b[0], distance])

edges.sort(key=lambda x: x[2])

data = {key: key for key in range(n + 1)}
rank = {key: 1 for key in range(n + 1)}

cnt = 0
weight = 0


def find(node: int) -> int:
    if node != data[node]:
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


while cnt < n - 1:
    a, b, c = edges.pop(0)
    if find(a) != find(b):
        union(a, b)
        cnt += 1
        weight += c

print(weight)
