import sys

sys.stdin = open('input.txt')

n = int(input())
data = list(map(int, input().split()))
m = int(input())


def palindrome(start: int, end: int) -> bool:
    # 0 2
    if start == end:
        return True

    if (end - start + 1) & 1:
        mid = (start + end) // 2
        left = mid - 1
        right = mid + 1
        while True:
            if not (0 <= left <= mid <= right < len(data)):
                return True

            if data[left] == data[right]:
                left -= 1
                right += 1
            else:
                return False
    else:
        left = (start + end) // 2
        right = left + 1
        while True:
            if not (0 <= left < len(data) and 0 <= right < len(data)):
                return True

            if data[left] == data[right]:
                left -= 1
                right += 1
            else:
                return False


for _ in range(m):
    ele1, ele2 = map(int, input().split())
    print(1) if palindrome(ele1 - 1, ele2 - 1) else print(0)
