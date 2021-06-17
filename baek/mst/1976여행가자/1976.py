import sys
sys.stdin = open('input.txt')

n = int(input())
m = int(input())
data = {key: key for key in range(n + 1)}
rank = {key: 1 for key in range(n + 1)}


def find(node: int):
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


for row in range(1, n + 1):
    temp = list(map(int, input().split()))
    for col in range(1, len(temp) + 1):
        if temp[col - 1] == 1:
            union(row, col)

tours = list(map(int, input().split()))
result = set([find(tour) for tour in tours])
if len(result) != 1:
    print("NO")
else:
    print("YES")