import heapq
import sys

sys.stdin = open('input.txt')

v, e = map(int, input().split())

start = int(input())

data = {key: [] for key in range(1, v + 1)}
for _ in range(e):
    s, e, weight = map(int, input().split())
    data[s].append((weight, e))

distance = [987654321] * (v + 1)

q = []
heapq.heappush(q, [0, start])
distance[start] = 0

while q:
    cost, x = heapq.heappop(q)
    for ncost, nx in data[x]:
        if distance[nx] > cost + ncost:
            distance[nx] = cost + ncost
            heapq.heappush(q, [distance[nx], nx])

for i in range(1, v + 1):
    print('INF') if distance[i] == 987654321 else print(distance[i])
