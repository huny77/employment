import sys
sys.stdin = open('input.txt')

def binary_search(left:int, right:int, target:str) -> str:
    while left<=right:
        mid = left + (right-left)//2
        if data2[mid] == target:
            return target
        elif data2[mid]>target:
            right= mid-1
        else:
            left = mid+1
    return ''
n, m = map(int, input().split())
data1, data2 = [], []
for _ in range(n):
    data1.append(input())
for _ in range(m):
    data2.append(input())

data2.sort()
answer = []
for data in data1:
    result = binary_search(0, len(data2)-1, data)
    if result!='':
        answer.append(result)

answer.sort()
print(len(answer))
for result in answer:
    print(result)
