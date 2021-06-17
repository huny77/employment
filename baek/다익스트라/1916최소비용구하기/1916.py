import heapq
import sys

sys.stdin = open('input.txt')

n = int(input())
m = int(input())
data = {key: [] for key in range(n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    data[a].append((c, b))

start, end = map(int, input().split())

q = [(0, start)]
distance = [987654321] * (n + 1)
distance[start] = 0

while q:
    cost, x = heapq.heappop(q)
    for ncost, nx in data[x]:
        if distance[nx] > ncost + cost:
            distance[nx] = ncost + cost
            heapq.heappush(q, (distance[nx], nx))
print(distance[end])
