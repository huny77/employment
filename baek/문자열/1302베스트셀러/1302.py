import sys

sys.stdin = open('input.txt')

n = int(input())
counter = {}
value = 1
for _ in range(n):
    line = input()
    if line not in counter:
        counter[line] = 1
    else:
        counter[line] += 1
        value = max(value, counter[line])
item = list(filter(lambda x: x[1] == value, counter.items()))
print(sorted(item, key=lambda x:x[0])[0][0])

