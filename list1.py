'''
vegetable = []
print (vegetable)

vegetable = ['Tomato', 'Carrot', 'Celery']
print (vegetable)

numbers = [1, 3, 5, 7]

mix = [1, "three", 5, "seven"]

odds = [1, 3, 5, 7]
print(odds[0])
print(odds[2])

odds = [1, 3, 5, 7]
odds[0] = 9
print(odds)

odds = [1, 3, 5, 7]
for i in range(len(odds)):
    print(odds[i])
'''

'''

#Practice

#1.
L = [1, 2, 3, 4, 5, 6, 7, 8]
print(L[4])

#2. 
L = [1, 2, 3, 4, 5, 6, 7, 8]
print(L[7])

#3. 
L = [1, 2, 3, 4, 5, 6, 7, 8]
L[3] = 10
print(L)

#4.
a = 0
L = [1, 2, 3, 4, 5, 6, 7, 8]
while (a<len(L)):
    print(L[a])
    a = a + 1

#5.
a = len(L)-1
L = [1, 2, 3, 4, 5, 6, 7, 8]
while (a>=0):
    print(L[a])
    a = a - 1

#6.
L = [1, 2, 3, 4, 5, 6, 7, 8]
print(len(L))


#Practice2

#1. 
L = [10, 7, 3, 3, 102, 6, 4, 8]
a = 0
while (a<len(L)):
    if (L[a]%2==0):
        print(L[a])
    a = a + 1

#2.
L = [1, 2, 3, 4, 5, 6, 7, 8]
a = 0
total = 0
while (a<len(L)):
    total = total + L[a]
    a = a + 1
print(total)

#3. 
#SKIP

#4. 
a = 0
grades = [89, 94, 33, 65, 74]
while (a<len(grades)):
    if (grades[a]>=90):
        print("A등급입니다")
    elif ((grades[a]<90) and (grades[a]>=80)):
        print("B등급입니다")
    elif ((grades[a]<80) and (grades[a]>=70)):
        print("C등급입니다")
    elif ((grades[a]<70) and (grades[a]>=60)):
        print("D등급입니다")
    elif (grades[a]<60):
        print("F등급, 낙제입니다")
    a = a+1
'''
'''
#5. 
L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0
b = 1
c = 0
while (L[a]-L[b]>=0):
    c = L[a] - L[b]
    b = b + 1

print(L[a])

#5.maybe?

L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0 #a the number's #
b = 0
max = L[a]
while (a<len(L)):
    if (max<L[a]):
        max = L[a]
    a = a + 1
print(max)

#6. yes

L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0 #a the number's #
b = 0
max = L[a]
while (a<len(L)):
    if (max>L[a]):
        max = L[a]
    a = a + 1
print(max)








#6. ANOTHER

L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0 #a the number's #
b = 0
max = L[a]
while (a<=len[L]):
    b = a + 1
    if (max>L[b]):
        max = L[b]
    elif (max<L[b]):
        a = a + 1
    print(max)

print(summ/len(L))
#6. 
L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = -1 #a the number's #
summ = 0
b = 0
c = 0
while (a<=len(L))
a = a + 1
    b = 0
    while (b<=len(L)):
        summ = L[a] - L[b]
        if (summ>0):
            b = b + 1
        elif (summ<0):
            b = b + 1
            c = c + 1
        elif (summ==0):
            b = b + 1
    if (c==9):
        print(L[a])


print(summ/len(L))

#7. 
L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0 #a the number's #
summ = 0
b = 1
c = 0
while (a<=len(L)):
    summ = L[a] + L[b] + summ
    b = b + 1
    a = a + 1

print(summ/len(L))


L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0 #a the number's #
summ = 0
while (a<len(L)):
    summ = summ + L[a]
    a = a + 1
print(summ/len(L))

L = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
summ = 0
for i in range (len(L)):
    summ = summ + L[i]
print(summ/len(L)) 
'''
#8.
l = [2, 4, 398, 287, 1, 349, 24, 10, 289, 50]
a = 0
c = 0
for a in range(len(l)):
    for i in range(len(l)-1-a):
        if (l[i]>l[i+1]):
            c = l[i+1]
            l[i+1] = l[i]
            l[i] = c
    
print(l)
'''
b = l[1]
l[1] = l[0]
l[0] = b
print(l)

a = l[4]
l[4] = l[9]
l[9] = a
print(l)


#1

 <b>
|   |
| 4 |
|ㅡㅡ|
#2

<l[1]>
|   |
| 2 |
|ㅡㅡ|
#3

 <l[0]>
|      |
| 4(b) |
|ㅡㅡㅡㅡ|
'''