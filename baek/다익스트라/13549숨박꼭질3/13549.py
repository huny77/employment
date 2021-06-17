import sys
from collections import deque

sys.stdin = open('input.txt')

n, m = map(int, input().split())

data = [-1] * 1000001

def bfs(start):
    q = deque([start])
    data[start] = 1
    while q:
        x = q.popleft()
        if x == m:
            print(data[m] - 1)
            return
        for nx in (x - 1, x + 1, x * 2):
            if not (0 <= nx < 1000001 and data[nx] == -1):
                continue
            if nx == x * 2 and x != 0:
                data[nx] = data[x]
                q.appendleft(nx)
            else:
                data[nx] = data[x] + 1
                q.append(nx)

    print(data[m] - 1)


bfs(n)
