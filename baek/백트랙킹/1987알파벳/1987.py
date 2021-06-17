import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())

data = [list(input()) for _ in range(n)]
answer = 0
cnt = 1
counter = {key:0 for key in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
counter[data[0][0]] = 1

def go(x: int, y: int, cnt: int) -> None:
    global answer
    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if not(0 <= nx < n and 0 <= ny < m):
            continue
        if counter[data[nx][ny]] == 0:
            counter[data[nx][ny]] = 1
            go(nx, ny, cnt + 1)
            counter[data[nx][ny]] = 0

go(0, 0, cnt)
print(answer)
