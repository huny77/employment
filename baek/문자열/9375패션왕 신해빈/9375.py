import sys
sys.stdin = open('input.txt')

for test in range(1, int(input()) + 1):
    n = int(input())
    counter = {}
    for _ in range(n):
        line = input().split()
        if line[1] not in counter:
            counter[line[1]] = 1
        else:
            counter[line[1]] += 1
    answer = 1
    for key, value in counter.items():
        answer *= value + 1
    print(answer-1)

