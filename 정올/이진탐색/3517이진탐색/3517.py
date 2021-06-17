n = int(input())
data = list(map(int, input().split()))
data.sort()
m = int(input())
data2 = list(map(int, input().split()))
answer = []
def binary_search(left:int, right:int, target:int) -> int:
    while left<=right:
        mid = left + (right-left) // 2
        if data[mid] == target:
            return mid
        elif data[mid]>target:
            right = mid-1
        else:
            left = mid+1
    return -1

for ele in data2:
    result = binary_search(0, len(data)-1, ele)
    answer.append(result)

print(*answer)