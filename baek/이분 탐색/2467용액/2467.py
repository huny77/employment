import sys

sys.stdin = open('input.txt')

n = int(input())

data = list(map(int, input().split()))
data.sort()

left = 0
right = len(data) - 1
total = 2e9
result = ()

while left < right:
    a, b = data[left], data[right]

    if abs(a + b) < total:
        total = abs(a + b)
        result = (data[left], data[right])

    if a + b < 0:
        left += 1
    else:
        right -= 1

print(result[0], result[1])
