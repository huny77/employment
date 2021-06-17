import sys
from collections import deque

sys.stdin = open('input.txt')

a, b = map(int, input().split())
n, m = map(int, input().split())
data = {key: [] for key in range(n + 1)}
distance = [-1 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    data[s].append(e)
    data[e].append(s)

q = deque([a])
distance[a] = 0
while q:
    x = q.popleft()
    for nx in data[x]:
        if distance[nx] == -1:
            distance[nx] = distance[x] + 1
            q.append(nx)
print(distance[b])
