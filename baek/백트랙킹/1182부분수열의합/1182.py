n, s = map(int, input().split())
data = list(map(int, input().split()))

answer = 0


def go(index: int, sum: int) -> None:
    global answer
    if index == len(data):
        if sum == s:
            answer += 1
        return

    go(index + 1, sum + data[index])
    go(index + 1, sum)


go(0, 0)
if s == 0:
    answer -= 1
print(answer)
