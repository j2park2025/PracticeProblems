arr = [0, 1, 1, 2, 2, 2, 3]
answer = [] 
lis = arr
for i in range(len(lis)-1, -1, -1): 
    print(i)
    if lis[i]==lis[i-1]:
        del lis[i]
        print(lis)
answer = lis
print(answer)              
