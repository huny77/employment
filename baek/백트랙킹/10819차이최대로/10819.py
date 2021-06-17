import sys

sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
sel = []
visited = [0] * n

answer = 0


def calc(sel: list) -> int:
    result = 0
    for i in range(len(sel) - 1):
        result += abs(sel[i] - sel[i + 1])
    return result


def go(cnt: int) -> None:
    global answer
    if cnt == n:
        answer = max(answer, calc(sel))
        return

    for i in range(n):
        if visited[i] == 1:
            continue
        visited[i] = 1
        sel.append(data[i])
        go(cnt + 1)
        sel.pop()
        visited[i] = 0


go(0)
print(answer)

