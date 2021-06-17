line = input()
answer = set()
for i in range(len(line)-1, -1, -1):
    answer.add(line[i:])

for ele in sorted(list(answer)):
    print(ele)