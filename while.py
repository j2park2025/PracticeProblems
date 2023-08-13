'''
n=0
while (n<5):
    print(n)
    n=n+1

n=10
while not(n<5):
    n=n-1
    print(n)

n=0
while True:
    print(n)
    n=n+1
'''
'''
n = 1
while n <10:
    print(n)
    n = n+1 


m=1
while m<10:
    n=1
    while n<10:
        print(m, "*", n, "=", m*n)
        n = n+1
    m = m+1
'''
'''
i = int(input("NUMBER:"))
n=2
while n<i:
    if (i%n==0):
        print("NOT PRIME")
        break
    n=n+1
if n == i:
    print("prime")
'''
'''
import random

# 1=addition
# 2=subtraction
# 3=multiplication
# 4=division
b = random.randint(10, 100)
c = random.randint(10, 100)
ans = 0
user_ans = 0
while (user_ans==ans):
    import random
    cal = random.randint(1, 3)
    b = random.randint(10, 100)
    c = random.randint(10, 100)
    if (cal==1):
        print(b, "+", c, "=?")
        ans = b+c
    elif (cal==2):
        print(b, "-", c, "=?")
        ans = b-c
    elif (cal==3):
        print(b, "*", c, "=?")
        ans = b*c
    user_ans = int(input(":"))
'''

'''
while i%2!=0:
    print("PRIME NUMBER")
while i%2==0:
    print("NOT A PRIME NUMBER")
'''

import random
ans = random.randint(1, 100)
userans = 0
trials = 0

while (userans!=ans):
    
    userans = int(input("Take a guess between 1-100"))
    if (userans<ans):
        print(userans, "is less than the answer")
        trials = trials + 1
    elif (userans>ans):
        print(userans, "is greater than the answer")
        trials = trials + 1
    elif (userans==ans):
        print("Correct! The answer was", ans, "you got it using", trials, "trials")
