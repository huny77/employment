import sys


def input():
    return sys.stdin.readline().rstrip()


s = input()
p = input()

stack = []
for word in s:
    stack.append(word)
    if len(stack) >= len(p):
        temp = "".join(stack[-len(p):])
        if temp == p:
            cnt = 0
            while cnt < len(p):
                cnt += 1
                stack.pop(-1)

print("".join(stack)) if stack else print("FRULA")
