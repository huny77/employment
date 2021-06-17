import sys

sys.stdin = open('input.txt')

n = int(input())
m = int(input())
edges = []
for _ in range(m):
    edges.append([*map(int, input().split())])
edges.sort(key=lambda x: x[2])

data = {key: key for key in range(n + 1)}
rank = {key: 1 for key in range(n + 1)}


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


cnt = 0
weight = 0

while cnt < n - 1:
    a, b, c = edges.pop(0)
    if find(a) != find(b):
        union(a, b)
        weight += c
        cnt += 1

print(weight)
