n = int(input())

d = [9999] * (n + 1)
d[3], d[5] = 1, 1

for i in range(6, n + 1):
    if d[i - 3] != 9999 or d[i - 5] != 9999:
        d[i] = d[i - 5] if d[i - 3] > d[i - 5] else d[i - 3]
        d[i] += 1

if d[n] == 9999:
    print(-1)
else:
    print(d[n])
