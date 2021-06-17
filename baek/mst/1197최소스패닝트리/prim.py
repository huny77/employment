#O(E+VlogV)
import heapq
import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())

edges = [list(map(int, input().split())) for _ in range(m)]
data = {key: [] for key in range(n + 1)}
visited = set()
for a, b, weight in edges:
    data[a].append((weight, b))
    data[b].append((weight, a))


def prim(node: int) -> int:
    q = []
    visited.add(node)
    result = 0
    for temp in data[node]:
        heapq.heappush(q, temp)

    while q:
        weight, node = heapq.heappop(q)
        if node not in visited:
            visited.add(node)
            result += weight

            for nweight, nnode in data[node]:
                if nnode not in visited:
                    heapq.heappush(q, (nweight, nnode))
    return result

print(prim(1))
