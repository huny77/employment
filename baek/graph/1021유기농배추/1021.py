import sys
sys.stdin = open('input.txt')

for test in range(1, int(input())+1):
    m, n, k = map(int, input().split())
    for _ in range(k):
        a, b = map(int, input().split())
        print(a, b)