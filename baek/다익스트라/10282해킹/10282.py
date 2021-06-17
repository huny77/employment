import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')


def dijkstra(start: int) -> None:
    distances = [987654321] * (n + 1)
    distances[start] = 0

    q = []
    heappush(q, (0, start))

    while q:
        cost, x = heappop(q)

        for ncost, nx in data[x]:
            if distances[nx] > cost + ncost:
                distances[nx] = cost + ncost
                heappush(q, (distances[nx], nx))

    distances = list(filter(lambda x: x != 987654321, distances))
    print(len(distances), max(distances))


for test in range(1, int(input()) + 1):
    n, d, c = map(int, input().split())
    data = {key: [] for key in range(n + 1)}
    for _ in range(d):
        a, b, s = map(int, input().split())
        data[b].append((s, a))
    dijkstra(c)
