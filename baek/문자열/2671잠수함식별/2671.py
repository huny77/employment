import re

line = input()

if re.fullmatch(r'(100+1+|01)+', line):
    print('SUBMARINE')
else:
    print('NOISE')
