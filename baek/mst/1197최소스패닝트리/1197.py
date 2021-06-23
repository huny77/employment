n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
# weight 순으로 정렬

cnt = 0
total_weight = 0
mst = []

data = {key: key for key in range(n + 1)}


def find(node: int) -> int:
    if node != data[node]:
        data[node] = find(data[node])
    return data[node]


def union(a: int, b: int) -> None:
    root1 = find(a)
    root2 = find(b)
    data[root2] = root1

# mst 최소 스패닝 트리 -> n vertex n-1 edge tree => spnning tree
# while mst 만드는 과정
# 정석 코드
while cnt < n - 1:
    a, b, c = edges.pop(0)

    if find(a) != find(b):
        union(a, b)
        mst.append([a, b])
        total_weight += c
        cnt += 1
print(total_weight)