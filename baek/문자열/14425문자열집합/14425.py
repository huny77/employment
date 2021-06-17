import sys

sys.stdin = open('input.txt')
n, m = map(int, input().split())

string_set = set()
for _ in range(n):
    string_set.add(input())
cnt = 0
for _ in range(m):
    line = input()
    if line in string_set:
        cnt += 1
print(cnt)

