import sys

sys.stdin = open('input.txt')

while True:
    line = input()
    if line == '.':
        break
    a = list(filter(lambda x: x == '[' or x == '(' or x == ')' or x == ']', line))
    stack = []
    if len(a) & 1:
        print('no')
    else:
        for ele in a:
            if ele == ')' and stack and stack[-1] == '(':
                stack.pop(-1)
            elif ele == ']' and stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                stack.append(ele)

        if stack:
            print('no')
        else:
            print('yes')
