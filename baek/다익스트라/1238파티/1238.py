import heapq


def dijkstra(node: int) -> list:
    distance = [987654321] * n
    distance[node] = 0
    q = [[0, node]]
    while q:
        cost, node = heapq.heappop(q)
        for nx, ncost in data[node]:
            if distance[nx] > ncost + cost:
                distance[nx] = ncost + cost
                heapq.heappush(q, [distance[nx], nx])
    return distance


n, m, x = map(int, input().split())
data = {key: [] for key in range(n)}
for _ in range(m):
    a, b, cost = map(int, input().split())
    data[a - 1].append([b - 1, cost])

answer = [0] * n
for i in range(n):
    result = dijkstra(i)
    if i == x - 1:
        for index, value in enumerate(result):
            answer[index] += value
    else:
        answer[i] += result[x - 1]
print(max(answer))
