import sys

sys.stdin = open('input.txt')

n = int(input())
counter = {}

for _ in range(n):
    line = input()
    temp = line.split(".")
    if temp[1] not in counter:
        counter[temp[1]] = 1
    else:
        counter[temp[1]] += 1
answer = []
for key, value in counter.items():
    answer.append([key, value])
for a, b in sorted(answer, key=lambda x:(x[0])):
    print(a, b)