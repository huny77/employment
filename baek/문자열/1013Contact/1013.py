import re
import sys
sys.stdin = open('input.txt')

n = int(input())
for _ in range(n):
    line = input()
    item = re.fullmatch('(100+1+|01)+', line)
    print('NO') if item is None else print('YES')