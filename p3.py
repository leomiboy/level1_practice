# coding: utf-8
num = int(input())
L = []
for i in range(num):
    line = input()
    line = line.split()
    L.append(line)
NL = []
for i in L:
    NL = NL + (list(range(int(i[0]),int(i[1])+1)))
NL = list(set(NL))
ans = len(NL)
for j in L:
    if int(j[1])+1 not in NL:
        ans = ans - 1
print(ans)
