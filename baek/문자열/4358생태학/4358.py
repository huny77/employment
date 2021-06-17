import sys

input = sys.stdin.readline

counter = {}
n = 0
while True:
    tree = input().rstrip()
    if not tree:
        break
    if tree in counter:
        counter[tree] += 1
    else:
        counter[tree] = 1
    n += 1

tree_lst = list(counter.keys())
tree_lst.sort()
for tree in tree_lst:
    print('%s %.4f' % (tree, counter[tree] / n * 100))