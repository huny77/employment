import re
import sys

sys.stdin = open('input.txt')

n = int(input())

for _ in range(n):
    if re.match('^[A-F]?A+F+C+[A-F]?$', input()):
        print('Infected!')
    else:
        print('Good')
