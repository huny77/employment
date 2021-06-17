import re
import sys
sys.stdin = open('input.txt')
line = input()
pattern = r'[^UCP]'
line = re.sub(pattern, '', line)
pattern2 = r'(.*U+.*C+.*P+.*C+.*)'
print('I love UCPC') if re.fullmatch(pattern2, line) else print('I hate UCPC')
