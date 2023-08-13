
vegetable = []
print(vegetable)
vegetable.append("tomato")
vegetable.append("carrot")
print(vegetable)

vegetable = ["tomato", "carrot", "onion"]
print(vegetable)
vegetable.insert(1, "cabbage")
print(vegetable)
vegetable.insert(3, "spinach") #this is the same as append
print(vegetable)

v = ['Tomato', 'Carrot', 'Celery']
del v[0]
print(v)

v = ['Tomato', 'Carrot', 'Celery', 'Onion', 'Spinach']
print(v)
v.pop()
print(v)
v.pop(1)
print(v)

ve = ['Tomato', 'Carrot', 'Celery', 'Onion', 'Spinach']
print(ve)
ve.remove('Celery')
print(ve)

v = ['Tomato', 'Carrot', 'Celery']
print(v)
v[1] = 'Onion'
print(v)
v[2] = 'Spinach'
print(v)


#append = adding something to the list(just adding)
#insert = inserting something in a specific location from a list
#del = removing a specific term from a list(not the word, but the term)
#pop = retunrs the value of the term when deleting?
#remove = delete the value itself when ordered to deleting something



l = [1,2,3,4]

deleted_value = l.pop(3)

#1
a = 1
L = []
while (a<9):
    L.append(a)
    a = a + 1

print(L)

#2 
L = []
while (len(L)<5):
    insert = str(input("insert item: "))
    L.append(insert)
    print(L)
    if(len(L)>=5):
        print("*WARNING* item full!")


#3


HELLO = L.pop('apple')
L.pop('apple')
print(L)
print(HELLO)

a = 0
L = ['apple', 'potato', 'phone', 'unbrella', 'apple', 'apple']
indexes = []
numb = []
for i in range(0, 6):
    if(L[i] == 'apple'):
        numb.append(i)
    elif(L[i]!= 'apple'):
        indexes.append(L[i])
print(indexes)
print(numb)

for i in range(5, -1, -1):
    if(L[i] == 'apple'):      
        L.pop(i)
print(L)


#4
L = [10, 384, 92, 84, 4, 93, 20]
a = L[0]
b = 0
for i in range(1, 7):
    if(a>L[i]):
        a = L[i]
        b = i
    
L.pop(b)
print(L)

#1 CHALLENGE 
P = [10, 384, 92, 84, 4, 93, 20]
h = 0
for i in range(len(P)):
    for a in range(len(P)-1-i):
        if(P[a]>P[a+1]):
            h = P[a+1]
            P[a+1] = P[a]
            P[a] = h
print(P)

