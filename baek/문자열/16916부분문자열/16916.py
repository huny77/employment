import sys

sys.stdin = open('input.txt')

p, s = input(), input()
import re

a = re.search(s, p)
if a:
    print(1)
else:
    print(0)
