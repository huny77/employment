import heapq
import sys

sys.stdin = open('input.txt')
test = 1
while True:
    n = int(input())
    if n == 0:
        break
    data = [list(map(int, input().split())) for _ in range(n)]
    distance = [[987654321] * n for _ in range(n)]
    q = [(data[0][0], 0, 0)]
    distance[0][0] = data[0][0]

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        cost, x, y = heapq.heappop(q)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if distance[nx][ny] > cost + data[nx][ny]:
                distance[nx][ny] = cost + data[nx][ny]
                heapq.heappush(q, (distance[nx][ny], nx, ny))

    print('Problem {}: {}'.format(test, distance[n - 1][n - 1]))
    test += 1
