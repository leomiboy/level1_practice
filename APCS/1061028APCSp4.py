# coding: utf-8
###輸入資料整理
num =int(input())
d1 = []
for i in range(2):
    line = list(map(int,input().split()))
    d1.append(line)
d2 = []
for i in range(num):
    d2.append([d1[0][i],d1[1][i]])
###找出全部排列
def p(x):###不使用套件的排列函數
    base = x
    ans = [[base[0]]]
    for i in range(1,len(base)):
        temp1 = []
        for j in range(len(ans)):
            for k in range(len(ans[0])+1):
                temp2 = ans[j] + [0] #避免陣列相同問題
                temp2.pop(-1)
                temp2.insert(k,base[i])
                temp1.append(temp2)
        ans = temp1
    return ans
allp = p(d1[0])
###計算答案
def cr(x):###設定消耗與對應的函數
    global num
    for i in range(num):
        if x == d2[i][0]:
            return d2[i][1]
Minsum = 999999999
for i in range(len(allp)):
    temp = allp[i][0]
    sum = 0
    for j in range(1,num):
        sum = sum + temp*cr(allp[i][j])
        temp = temp + allp[i][j]
    if Minsum > sum:
        Minsum = sum
print(Minsum)
