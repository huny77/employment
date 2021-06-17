from collections import deque

n, m, k, x = map(int, input().split())
data = {key: [] for key in range(n)}
distance = [-1] * n
for i in range(m):
    a, b = map(int, input().split())
    data[a - 1].append(b - 1)

q = deque([x - 1])
distance[x - 1] = 0

while q:
    x = q.popleft()
    for nx in data[x]:
        if distance[nx] == -1:
            distance[nx] = distance[x] + 1
            q.append(nx)

result = [ele1 for ele1, ele2 in zip(range(n), distance) if ele2 == k]
if not result:
    print(-1)
else:
    for ele in result:
        print(ele + 1)
