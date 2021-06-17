import sys
sys.stdin = open('input.txt')

def lower_bound(left: int, right: int, target: int) -> int:
    result = left-1
    while left<=right:
        mid = left + (right - left) // 2
        if data2[mid]>=target:
            right = mid-1
        else:
            result = mid
            left = mid+1
    return result


for test in range(1, int(input())):
    n, m = map(int, input().split())
    data1 = list(map(int, input().split()))
    data2 = list(map(int, input().split()))
    data2.sort()
    answer = 0
    for data in data1:
        answer += lower_bound(0, len(data2)-1, data)+1

    print(answer)
