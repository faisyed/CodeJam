n = int(input())
ls = list(map(int,input().split()))

x = 1
for i in range(2, n+1):
    x^=i
y = ls[0]
for i in range(1, len(ls)):
    y^=ls[i]
print(x^y)