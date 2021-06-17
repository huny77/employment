import sys

sys.stdin = open('input.txt')

answer = []
n = int(input())
for _ in range(n):
    line = input().split()
    answer.append([line[0], int(line[1]), int(line[2]),int(line[3]) ])
answer.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for result in answer:
    print(result[0])
