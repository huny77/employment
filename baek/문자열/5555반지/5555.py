import sys
import re
sys.stdin = open('input.txt')
pattern = input()
n = int(input())
cnt = 0
for _ in range(n):
    string = input()
    for _ in range(len(string)):
        if re.match(pattern, string):
            cnt+=1
            break
        else:
            string = string[1:]+string[:1]
print(cnt)