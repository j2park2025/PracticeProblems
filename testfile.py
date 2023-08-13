'''
array = [1, 5, 2, 6, 3, 7, 4]
abe = array[2:5]
print(abe)
'''
'''
def solution(n):
    primes = [1] * (n+1)
    for k in range(2, n):
        for h in range(k*2, n+1, k):
            primes[h] = 0
    print(primes)
solution(10)

def solution(answers):
    
    answer = []
    scoreO = 0
    scoreT = 0
    scoreH = 0
    one = [1,2,3,4,5]
    two = []
    three = []   
 
    
    
    
    for first in range(0, len(answers)):
        if(one[first%len(one)]==answers[first]):
            scoreO = scoreO + 1
        if(two[first]==answers[first]):
            scoreT = scoreT + 1
        if(three[first]==answers[first]):
            scoreH = scoreH + 1

    print(scoreT, scoreH, scoreO)

    ma = max(scoreH, scoreT, scoreO)
    if (ma == scoreO) :
        answer.append(1)
    if (ma == scoreT):
        answer.append(3)

solution([1, 5, 3, 2, 4, 3, 1, 2, 3, 4, 5])

def solution(x):
    tens = 0
    tn = 0
    ones = 0
    hundreds = 0
    hn = 0
    thousands = 0
    number = x
    summ = 0
    rep = 0
    last_digit = 0
     
    if(((number)>0) and (number<10)):
        rep = 1

    elif(((number)>10) and (number<100)):
        rep = 2
        for i in range(0, 10):
            if(number%10==0):
                tens = number/10
                ones = ones
                break
            number = number -1
            ones = ones + 1

    elif(((number)>100) and (number<1000)):
        rep = 3
        for i in range(0, 100):
            if(number%100==0):
                hundreds = number/100
                number = tn
                for i in range(0, 10):
                    if(number%10==0):
                        tens = number/10
                        ones = ones
                        break
                    number = number -1
                    ones = ones + 1
            number = number -1
            tn = tn + 1

    elif(((number)>1000) and (number<10000)):
        rep = 4
        for i in range(0, 1000):
            if(number%1000==0):
                thousands = number/1000
                number = hn
                for i in range(0, 100):
                    if(number%100==0):
                        hundreds = number/100
                        number = tn
                        for i in range(0, 10):
                            if(number%10==0):
                                tens = number/10
                                ones = ones
                                break
                            number = number -1
                            ones = ones + 1
                    number = number -1
                    tn = tn + 1
            number = number -1
            hn = hn + 1
    elif(number==10000):
        rep = 5
        thousands = 1
        hundreds = 0
        tens = 0
        ones = 0
        
    

    if(x%(thousands+hundreds+tens+ones)==0):
        answer = True
    if(x%(thousands+hundreds+tens+ones)!=0):
        answer = False
    
    
            
    return answer

print(solution(234))
'''

# def solution(n):
#     answer = 0
#     lis = []
#     reorder = []
#     ten = 1
#     times = 0
#     so = n
#     sumn = 0
    
#     for h in range(n):
#         if(so<10):
#             lis.append(so)
#             break
#         if(so%10==0):
#             for j in range(len(lis)):
#                 sumn = sumn + (lis(j))
#             lis.append(h-(sumn))
#             so = so/10
#         if(so==10):
#             lis.append(1)
#             break
#         so = so-1
    
#     reorder = sort(lis())
#     reorder = reverse(lis())
#     return lis()



# for i in range(len(reorder)):
#     answer = reorder[i]*10 + reorder[i+1]

# solution(123)

def solution(n):
    answer = 0
    lis = []
    reorder = []
    times = 0
    so = n
    a = 0

    for h in range(n):
        if(so<10):
            lis.append(so)
            break
        if(so%10==0):
            lis.append(times)
            so = so/10
            times = 0
        if(so==1):
            lis.append(1)
            break
        so = so-1
        times = times + 1
    
    lis.sort()
    lis.reverse()
    a = lis[0]

    for i in range(len(lis)-1):
        answer = a*10 + lis[i+1]
        a = answer

    return answer

# #8*10 + 7
# #87*10 + 3
# #873*10 + 2
# #8732*10 +1
# #87321*10 +1
# #873211

print(solution(118372))
