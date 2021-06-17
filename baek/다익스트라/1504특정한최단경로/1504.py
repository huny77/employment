import heapq
import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())

data = {key: [] for key in range(n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((c, b))
    data[b].append((c, a))
v1, v2 = map(int, input().split())


def dijkstra(node:int, end:int) -> int:
    distance = [999999999] * (n + 1)
    q = [[0, node]]
    distance[node] = 0
    while q:
        cost, x = heapq.heappop(q)
        for ncost, nx in data[x]:
            if distance[nx] > ncost + cost:
                distance[nx] = ncost + cost
                heapq.heappush(q, [distance[nx], nx])
    return distance[end]

answer = 0
answer +=  dijkstra(1, v1)
answer +=  dijkstra(v1, v2)
answer +=  dijkstra(v2, n)

print(answer)
