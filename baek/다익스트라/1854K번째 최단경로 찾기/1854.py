import sys
sys.stdin = open('input.txt')

from collections import defaultdict
from heapq import heappop, heappush

INF = int(1e9)


def dijkstra(start):
    q = [[0, start]]
    distance = [[INF] * (k) for i in range(n + 1)]
    distance[start][0] = 0
    while q:
        cost, x = heappop(q)
        for nx, ncost in data[x]:
            if distance[nx][k - 1] > ncost + cost:
                distance[nx][k - 1] = ncost + cost
                distance[nx] = sorted(distance[nx])
                heappush(q, [ncost + cost, nx])
    return distance


n, m, k = map(int, sys.stdin.readline().split())
data = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    data[a].append([b, c])

distance = dijkstra(1)
for i in range(1, n + 1):
    if distance[i][k - 1] == INF:
        print(-1)
    else:
        print(distance[i][k - 1])
