n = 10453
answer = 0
lis = []
reorder = []
times = 0
so = n
a = 0

while so >= 10: # 10345
    if (0==so%10):
        lis.append(0)
        print(so%10)
    elif (so%10!=0):
        lis.append(so%10) #5, 4, 3, 
    so = int(so/10)
lis.append(so) #1
print(lis)     

#10의 배수

lis.sort()
lis.reverse()
print(lis)
a = lis[0]
#list 
for i in range(len(lis)-1):
    answer = a*10 + lis[i+1]
    a = answer
print(answer)
