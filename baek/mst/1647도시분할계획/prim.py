import heapq
import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())

data = {key: [] for key in range(n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((c, b))
    data[b].append((c, a))


def prim(x: int) -> int:
    q = []
    visited = set()
    visited.add(x)
    result = 0
    for temp in data[x]:
        heapq.heappush(q, temp)
    value = 0
    while q:
        weight, x = heapq.heappop(q)
        if x not in visited:
            visited.add(x)
            result += weight
            value = max(value, weight)

            for nweight, nx in data[x]:
                if nx not in visited:
                    heapq.heappush(q, (nweight, nx))
    return result - value


print(prim(1))
