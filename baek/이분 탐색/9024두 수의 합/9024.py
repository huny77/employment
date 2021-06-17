import sys

sys.stdin = open('input.txt')

INF = 987654321
for test in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    data.sort()

    cnt = 0
    result = INF

    for i in range(len(data) - 1):
        left = i + 1
        right = len(data) - 1

        while left <= right:
            mid = left + (right - left) // 2
            sum = data[mid] + data[i]
            if sum > k:
                right = mid - 1
            elif sum <= k:
                left = mid + 1
            if abs(k - sum) < result:
                result = abs(k - sum)
                cnt = 1
            elif abs(k - sum) == result:
                cnt += 1
    print(cnt)
