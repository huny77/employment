n = int(input())
data = sorted(list(map(int, input().split())))


def lower_bound(left: int, right: int, target: int) -> int:
    result = right + 1
    while left <= right:
        mid = left + (right - left) // 2
        if data[mid] >= target:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


best = 1<<31
v1, v2 = 0, 0
for left in range(len(data) - 1):
    result = lower_bound(left + 1, n - 1, -data[left])
    if left < result - 1 and abs(data[left] + data[result - 1]) < best:
        best = abs(data[left] + data[result - 1])
        v1, v2 = data[left], data[result - 1]

    if result < n and abs(data[left] + data[result]) < best:
        best = abs(data[left] + data[result])
        v1, v2 = data[left], data[result]

print(v1, v2)
