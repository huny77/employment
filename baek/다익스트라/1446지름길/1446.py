n, m = map(int, input().split())
data = {key: [] for key in range(10001)}
for _ in range(n):
    a, b, c = map(int, input().split())
    data[a].append((c, b))

distance = [d for d in range(m + 1)]

for i in range(m + 1):
    if i != 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)
    for w, e in data[i]:
        if e <= m and distance[e] > w + distance[i]:
            distance[e] = w + distance[i]

print(distance[m])
