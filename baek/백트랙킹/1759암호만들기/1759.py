n, m = map(int, input().split())
data = input().split()
data.sort()
answer = set()
sel = []


def go(index: int, cnt: int, one: int, two: int) -> None:
    global answer
    if cnt == n:
        if one >= 1 and two >= 2:
            answer.add(''.join(sel))
        return

    if index >= len(data):
        return
    sel.append(data[index])
    if data[index] in 'aeiou':
        go(index + 1, cnt + 1, one + 1, two)
    else:
        go(index + 1, cnt + 1, one, two + 1)
    sel.pop()

    go(index + 1, cnt, one, two)


go(0, 0, 0, 0)
for ele in sorted(list(answer)):
    print(ele)
