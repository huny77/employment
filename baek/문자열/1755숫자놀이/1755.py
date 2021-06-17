import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split())
mapper = {
    '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five'
    , '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'
}
data = []
for ele in range(n, m + 1):
    string = ''
    for word in list(str(ele)):
        string += mapper[word]
    data.append([string, ele])
cnt = 0
for ele in sorted(data, key=lambda x: x[0]):
    print(ele[1], end=' ')
    cnt += 1
    if cnt % 10 == 0:
        print()
