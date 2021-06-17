import sys

sys.stdin = open('input.txt')


def binary_search(left: int, right: int, target: int) -> bool:
    while left <= right:
        mid = left + (right - left) // 2
        if data3[mid] == target:
            return True
        elif data3[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return False


n = int(input())
data = list(map(int, input().split()))
m = int(input())
data2 = list(map(int, input().split()))

data3 = sorted(data2)
counter = {}
for ele in data2:
    if ele not in counter:
        counter[ele] = 0

for ele in data:
    if ele in counter:
        counter[ele] += 1
    else:
        if binary_search(0, len(data3) - 1, ele):
            counter[ele] = 1

for word in data2:
    print(counter[word], end=' ')
