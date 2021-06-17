import sys

sys.stdin = open('input.txt')
n = int(input())

company = {}
for _ in range(n):
    a, b = input().split()
    if b == 'enter':
        company[a] = 1
    else:
        company[a] = 0

item = sorted(list(map(lambda x: x[0], filter(lambda x: x[1] == 1, company.items()))), reverse=True)

for ele in item:
    print(ele)

