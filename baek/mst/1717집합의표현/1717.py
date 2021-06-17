import sys
n, m = map(int, sys.stdin.readline().rstrip().split())

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


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 0:
        union(b, c)
    else:
        root1 = find(b)
        root2 = find(c)
        if root1 == root2:
            print('YES')
        else:
            print('NO')
