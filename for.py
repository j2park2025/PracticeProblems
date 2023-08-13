#count =0
#for i in range(10):
#    count=count + 1
#    print(count)

#for i in range(5):
    #print(i)

#for i in range(5, 10):
 #   print(i)

#for i in range(1, 10, 3):
#    print(i)
#for i in range(20, 10, -2):
  #  print(i)

#for i in range(1, 11):
#    if i%2==1:
    #   print(i)

#range(n1) # 0 ~ n1-1
#for i in range(10):
#  print(i)
#range(n1,n2) # n1 ~ n2-1
#for i in range(5, 10):
#  print(i)
#range(n1,n2,n3) #n1 ~ n2-1 n3 interval 
#for i in range(5, 15, 3):
#  print(i)

'''
# 10 ~ 0
for i in range(10, -1, -1):
    print(i)

#print("*"*5)

i = int(input("dan?"))
for a in range(1, 11):
    print(a," x ", i, " = ", i*a)

for a in range(2, 10):
    for i in range(1, 11):
        print(a," x ", i, " = ", i*a)
'''
'''
print("*" * 5)
print(" "*4 + "*"*1)
'''
'''
for a in range(1, 6):
    print("*" * a)
    '''
'''
s+a = 5
s = 5-a
s a 
4 1
3 2 
2 3 
1 4
0 5
'''
'''
for a in range(1, 6):
    print(" " * (5-a) + "*"* a)

print("   ")

for i in range(5, 0, -1):
    print("*"*i)

print("   ")

for i in range(1, 6):
    print("*"*i)
for i in range(5, 0, -1):
    print("*"*i)

print("   ")
'''
# absolute value 
# |-5|
'''
for a in range(1, 6):
    print(" " * (5-a) + "*"* a)
for a in range(1, 6):
    print(" " * a + "*"* (5-a))

for x in range(1, 10):
    print("*" * (-abs(x-5)+5) )

print("   ")
'''
for x in range(1, 10):
    print(" " * (abs(x-5)) + "*" * -(abs(x-5)+5))

'''
print("    ")

for i in range(3, -1, -1):
        print(" "* i + "*" * (7 - i*2))


^^^*
^^***
^*****
*******
x*2 + y = 7
x=(y-7)/2
x y
3 1
2 3
1 5
0 7
an=4+(n-1) n+3
x+y = x+3..?
x+y=y+3

x y

'''
'''
print("    ")

for i in range(0, 4):
        print(" " * i + "*"* (7 - i*2))

print(" ")
'''
'''
x y
3 1
2 3
1 5

^^^*
^^***
^*****
'''
'''
for i in range(3, 0, -1):
        print(" " * i + "*" * (7 - i*2))
for i in range(1, 4):
        print(" " * i + "*" * (7 - i*2))
'''


#for i in range(-2, 1):
#    print(" " * abs(i) + "*" * abs(i/2))

for i in range(3, 0, -1):
    print(" " * (i) + "*" * (7 - i*2))
for i in range(2, 4):
    print(" " * (i) + "*" * (7 - i*2))

'''
x y
2 1 - 3   y=-x/2
1 3 - 4
0 5 - 5

1 3 - 4
2 1 - 3
'''
'''
  *
 ***
*****
'''


# for i in range(1, 11, 2):
# # 1-10 까지, 2 씩 증가
# for i in range(1, 11):
# # 1-10 까지, 1 씩 증가
# for i in range(5):
# # 0-4 까지, 1 씩 증가