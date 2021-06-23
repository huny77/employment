sel = []
answer = []
flag = False


def go(index: int, target: int, data: list) -> None:
    global sel, flag, answer
    if sum(sel) == target and len(sel) > len(answer):
        answer = sel[:]
        flag = True
        return
    # backtrack condition
    if flag or sum(sel) > target or index >= len(data):
        return

    sel.append(data[index])
    go(index + 1, target, data)
    sel.pop(-1)

    go(index + 1, target, data)


def solution(N: int) -> list:
    # write your code in Python 3.6
    # 1,000,000,000 -> odd 500,000,000
    # not dfs
    data = [ele for ele in range(1, N) if ele & 1 != 0]
    go(0, N, data)
    print(answer)
    return answer

# 찾아보자
