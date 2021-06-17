n = input()
d1 = [-1] * 46
d2 = [-1] * 46

d1[1] = 0
d2[1] = 1
d1[2] = 1
d2[2] = 1

for i in range(3, n + 1):
    d1[i] = d1[i - 1] + d1[i - 2]
    d2[i] = d2[i - 1] + d2[i - 2]

print(d1[n], d2[n])