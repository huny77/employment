import heapq


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


def calc_distance(a: list, b: list) -> float:
    x1, y1 = a
    x2, y2 = b
    return (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5


n, m = map(int, input().split())

cnt = 0
data = {key: key for key in range(n + 1)}
rank = {key: 1 for key in range(n + 1)}
nodes = [0]
for _ in range(n):
    nodes.append(list(map(int, input().split())))

for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

# 이거 조금 특이한 거 같다.
q = []
for i in range(1, n):
    for j in range(i + 1, n + 1):
        distance = calc_distance(nodes[i], nodes[j])
        heapq.heappush(q, [distance, i, j])

while q:
    cost, a, b = heapq.heappop(q)

    if find(a) != find(b):
        union(a, b)
        cnt += cost

print(format(cnt, '.2f'))
