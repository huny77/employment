# 백준 색종이 붙이기 문제하고 비슷할지도.
def is_mark(y: int, x: int) -> bool:
    if not (0 <= x < w - 1 and 0 <= y < h - 1):
        return False

    if data[y][x] == 0 and data[y + 1][x] == 0 and data[y][x + 1] == 0 and data[y + 1][x + 1] == 0:
        return True
    else:
        return False


def mark(y: int, x: int, flag: int) -> None:
    data[y][x] = data[y][x + 1] = data[y + 1][x] = data[y + 1][x + 1] = flag


def go(x: int, y: int, cnt: int) -> None:
    global answer
    if y == w:
        ans = max(ans, cnt)
        return

    if x == h:
        go(0, y + 1, cnt)
        return

    if x == 0:
        col = 0
        for row in range(h):
            if data[row][y] == 1:
                col += 2 ** row

        if dp[y][col] >= cnt:
            return
        else:
            dp[y][col] = cnt

    if is_mark(x, y):
        mark(x, y, 1)
        go(x + 1, y, cnt + 1)
        mark(x, y, 0)

    go(x + 1, y, cnt)


for test in range(1, int(input()) + 1):
    h, w = map(int, input().split())

    data = [list(map(int, input().split())) for _ in range(h)]
    dp = [[-1 for _ in range(2 ** 10)] for _ in range(w)]  # W x 1024

    answer = 0

    go(0, 0, 0)

    print("#" + str(test), answer)
