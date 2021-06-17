import sys

sys.stdin = open('input.txt')

n = int(input())
counter = {}
for _ in range(n):
    line = int(input())
    if line not in counter:
        counter[line] = 1
    else:
        counter[line] += 1

differ1, differ2 = None, 0
for key, value in counter.items():
    if value > differ2:
        differ1, differ2 = key, value
    elif differ2 == value and differ1> key:
        differ1 = key
print(differ1)

