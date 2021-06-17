import itertools
import sys
from collections import deque

sys.stdin = open('sample1.txt')

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(chicken: list) -> int:
    global min_chicken
    q = deque()
    distance = [[-1] * m for _ in range(n)]
    cnt1 = 0
    for row, col in chicken:
        q.append([row, col])
        distance[row][col] = 0
        cnt1 += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if distance[nx][ny] == -1 and data[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append([nx, ny])
                cnt1 += 1
    if min_chicken < cnt1:
        return 0
    else:
        min_chicken = cnt1

    cnt = 0
    for row in range(n):
        for col in range(m):
            if distance[row][col] == -1 and data[row][col] == 0:
                cnt += 1

    return cnt


for test in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    data=[]
    zero = []
    chicken = []
    for row in range(n):
        line = list(map(int, input().split()))
        data.append(line)
        for col in range(m):
            if data[row][col] == 0:
                zero.append([row, col])
            elif data[row][col] == 2:
                chicken.append([row, col])

    answer = 0
    min_chicken = 987654321
    for line in itertools.combinations(zero, 3):
        for row, col in line:
            data[row][col] = 1
        answer = max(answer, bfs(chicken))
        for row, col in line:
            data[row][col] = 0

    print('#{} {}'.format(test, answer))
