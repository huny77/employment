import sys
from itertools import combinations

sys.stdin = open('sample3.txt')


def check(A: tuple, B: tuple) -> tuple:
    """
    상성표에 따른 결과 처리
    :param A:
    :param B:
    :return:
    """
    index_a, a = A
    index_b, b = B
    if a == b:
        # 점수가 같은면 뒷쪽 문제 조건
        return A if index_a < index_b else B
    return A if (a, b) == (1, 2) or (a, b) == (2, 3) or (a, b) == (3, 1) else B
    #  조건표에 따른 출력 나머지는 무조건 B


for test in range(1, int(input()) + 1):
    line = list(map(int, input().split()))
    data = []
    for index in range(len(line)):
        data.append((index, line[index]))

    win, fail = [], []
    for pointer in range(0, len(data) - 1, 4):
        comb_calc = []
        counter = {}
        for val1, val2 in list(combinations(data[pointer:pointer + 4], 2)):
            result = check(val1, val2)
            if result not in counter:
                counter[result] = 1
            else:
                counter[result] += 1
            # 카운팅을 해서 하나씩 늘려준다.
            comb_calc.append(check(val1, val2))

        sample =[[key, value] for key, value in counter.items()]
        for i in range(len(sample)):
            sample[i].append(i)
        sample.sort(key=lambda x:(-x[1], x[2]))
        # 인덱스를 같이 넣어줘야 제일 많이 한 것을 구하고 같으면
        # 인덱스 순으로 정렬을 할 수 있다. (제일 헷갈림.)

        win.append(sample[0][0])
        fail.append(sample[1][0])

    gang_16 = []
    for a, b in zip(win, reversed(fail)):
        # 16강 부터는 뒤집어 준다. (문제 조건)
        gang_16.append(check(a, b))

    gang_8 = []
    for pointer in range(0, 7, 2):
        # 8 강 8명
        va1, va2 = gang_16[pointer:pointer + 2]
        # 위에서 부터 차례로 2명씩 구하면 된다.
        gang_8.append(check(va1, va2))

    gang_4 = []
    for pointer in range(0, 3, 2):
        # 4강 4명
        va1, va2 = gang_8[pointer:pointer + 2]
        gang_4.append(check(va1, va2))

    result1, result2 = gang_4
    # 2강(?) or 결승
    answer = check(result1, result2)
    print('#{} {}'.format(test, answer[0]))
