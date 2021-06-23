import sys
sys.stdin = open('input.txt')


def find(node: int) -> int:
    if data[node] != node:
        data[node] = find(data[node])
    return data[node]


def union(a: int, b: int) -> None:
    root1 = find(a)
    root2 = find(b)
    data[root1] = root2


n, m = map(int, input().split())  # 집의 개수, 길의 개수 입력받기
edges = [list(map(int, input().split())) for _ in range(m)]
edges.sort(key=lambda x: x[2])
data = {key: key for key in range(n + 1)}

last = []  # 선택된 간선

answer = 0
for a, b, weight in edges:
    if find(a) != find(b):
        union(a, b)
        answer += weight
        last = weight

answer -= last
print(answer)
