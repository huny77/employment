import sys, re

sys.stdin = open('input.txt')
n = int(input())

pattern = input().replace('*', '([a-z]*)')
for _ in range(n):
    target = input()
    value = re.fullmatch(pattern, target)
    if value is not None:
        print('DA')
    else:
        print('NE')
