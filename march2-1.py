a=[]
m=int(input('enter the no. of rows: '))
n=int(input('enter no. of columns: '))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    a.append(row)
print(a)
b=[]
m=int(input('enter the no. of rows: '))
n=int(input('enter no. of columns: '))
for i in range(m):
    row=[]
    for j in range(n):
        k=int(input())
        row.append(k)
    b.append(row)
print(b)
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j]=c[i][j]+a[i][k]*b[k][j]
print('resultant matrix is: ')
for i in range(m):
    for j in range(n):
        print(c[i][j],end=' ')
    print()
