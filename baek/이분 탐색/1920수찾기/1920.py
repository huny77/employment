import sys
sys.stdin = open('input.txt')

def binary_search(left: int, right: int, target: int) -> int:
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] == target:
            return 1
        elif data[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return 0


n = int(input())
data = list(map(int, input().split()))
data.sort()

m = int(input())
data2 = list(map(int, input().split()))
for target in data2:
    print(binary_search(0, len(data) - 1, target))
