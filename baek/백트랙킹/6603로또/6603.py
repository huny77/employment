import sys
sys.stdin = open('input.txt')
def go(index: int, cnt: int) -> None:
    if cnt == 6:
        print(*sel)
        return
    if index >= len(b):
        return
    sel.append(b[index])
    go(index + 1, cnt + 1)
    sel.pop()

    go(index + 1, cnt)


while True:
    line = list(map(int, input().split()))
    if len(line) == 1:
        break
    a, b = line[0], line[1:]
    sel = []
    go(0, 0)
    print()
