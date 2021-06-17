import sys

sys.stdin = open('sample4.txt')


def calc(origin: str, change: str, num: int) -> int:
    if origin == change:
        return 0
    mapper = {
        # 시계 반시계
        1: [1, 1],
        2: [2, 3],
        3: [4, 5],
        4: [6, 7]
    }
    counter_clock = ord(origin)
    a, b = 0, 0
    clock = ord(origin)
    while True:
        counter_clock += 1
        a += 1
        if counter_clock == 91:
            counter_clock = 65
        if counter_clock == ord(change):
            break

    while True:
        clock -= 1
        b += 1
        if clock == 64:
            clock = 90
        if clock == ord(change):
            break
    return min(a*mapper[num][0], b*mapper[num][1])





for test in range(1, int(input()) + 1):
    a = input()
    b = input()
    i = 1
    answer = 0
    for ele1, ele2 in zip(a, b):
        # print(ele1, ele2)
        result = calc(ele1, ele2, i)
        answer+=result
        # print(result, answer)
        i += 1
    print('#{} {}'.format(test, answer))
