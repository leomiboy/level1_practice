# coding: utf-8
####輸入資料
fig = []
pot = []
while 1:
    a = input()
    if a =='*':
        break
    else:
        fig.append(a)
while 1:
    b = input()
    if b =='9999.9 9999.9':
        break
    else:
        pot.append(b)

####定義檢核函數
def check(p,f):
    pd = list(map(float,p.split()))
    fd = list(f.split())
    if fd[0]=="r":
        fd.pop(0)
        fd = list(map(float,fd))
        if (fd[0]<pd[0])&(pd[0]<fd[2])&(fd[1]>pd[1])&(pd[1]>fd[3]):
            return 1
        else:
            return 0
    else:
        fd.pop(0)
        fd = list(map(float,fd))
        if (fd[0]-pd[0])**2+((fd[1]-pd[1]))**2 < (fd[2])**2:
            return 1
        else:
            return 0
    
for i in range(1,len(pot)+1):
    c = 0
    for j in range(1,len(fig)+1):
        if check(pot[i-1],fig[j-1])== 1:
            print(f'Point {i} is contained in figure {j}')
            c = 1
    if c == 0:
        print(f'Point {i} is not contained in any figure') 
