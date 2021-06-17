import sys

sys.stdin = open('input.txt')

n = int(input())
result = set()

for _ in range(n):
    line = input()
    result.add(line)
result = sorted(list(result), key=lambda x: (len(x), x))
for re in result:
    print(re)
