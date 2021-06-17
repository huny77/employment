import heapq
import sys

sys.stdin = open('input.txt')

n = int(input())

data = [list(input()) for _ in range(n)]

q = []
distance = [[987654321] * n for _ in range(n)]
distance[0][0] = 0
q.append((0, 0, 0))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while q:
    cost, x, y = heapq.heappop(q)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not (0 <= nx < n and 0 <= ny < n):
            continue

        if data[nx][ny] == '1' and distance[nx][ny] > cost:
            distance[nx][ny] = distance[x][y]
            q.append((distance[nx][ny], nx, ny))

        if data[nx][ny] == '0' and distance[nx][ny] > cost + 1:
            distance[nx][ny] = distance[x][y] + 1
            heapq.heappush(q, (distance[nx][ny], nx, ny))

print(distance[n - 1][n - 1])
