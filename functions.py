'''

print("Hello World")

def function0():
    pass

function0()

def function1():
    print("안녕!")
    print("Nice to Meet You!")
    print("I am Susie!")

function1()

def function2(a):
    return a*5

function2(5)

k = function2(5)
print(k)

def function3(a, b):
    return a+b

print(function3(4, 10))

age1 = 10
age2 = 15
name1 = "John"
name2 = "Alice"

def function4(name, age):
    print(name, "is", age, "years old.")

function4(name1, age1)

def function5(a):
    print(a)
    print("still inside function5 function")
    return 3*a

f = function5(10)
print("f's value?: ", f)



#1
def hello(a):
    print("Hello,", a)

hello("Jamie")

#2
def area(base, height):
    return base*height/2

print(area(4, 6))

#3
def mile(km):
    return km*0.62
    
print(5, "km is equal to", mile(5), "miles.")



#4
def divisor(b):
    l = []
    for i in range(1, b+1):
        if (b%(i)==0):
            l.append(i)
    return l

print("divisors are", divisor(30))

#5
name1 = "Hana"
height1 = 2.0 #Hana's height
weight1 = 90 #Hana's weight

name2 = "Duri"
height2 = 1.8
weight2 = 70

name3 = "Sami"
height3 = 2.5
weight3 = 160

#how to get bmi: kg/m^2

def BMI(name, weight, height):
    return name, weight/(height**2)

print("BMI is", BMI(name1, weight1, height1))

#2
import math
def hurray(a, b, c):
    a = (b**2)-(4*a*c)
    x = (-b + math.sqrt(a))/(2*a)
    return x

print("x=", hurray(1, 5, 6))



#3 HOMEWORK
# 1, 1, 2, 3, 5
def fibonacci(n):
    a = 1
    b = 1
    c = 0
    for i in range (n-2):
        c = a
        a = b
        b = c+b
    return b

def fibonacci1(n):
    l = [1, 1]
    for i in range (n-2):
        l.append(l[len(l)-1] + l[len(l)-2])
    return l[len(l)-1]
'''
#f(n) = f(n-1) + f(n-2)
def fibonacci2(n):
    if(n==1):
        return 1
    if(n==2):
        return 1
    a = fibonacci2(n-1) + fibonacci2(n-2)
    return a
print("number for your fibonacci sequence", fibonacci2(5))

'''
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a = i * a
    return a

print("Your factorial number is", factorial(6))


# 5! = 5*4! = 5*4*3! = 2*1
def factorial1(n): # a function call itself -> Recursion 
    if n == 1:
        return 1
    return n * factorial1(n-1)
print("Your factorial number is", factorial1(6))

'''

