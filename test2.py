
# # # def solution(arr1, arr2):
# # #     answer = [[]]
# # #     for i in range(len(arr1)):
# # #         for a in range(len(arr1)):
# # #             answer[i].append((arr1[i][a])+(arr2[i][a]))

# # # solution([[1, 2], [2, 3]], [[3, 4], [5, 6]])

# # def solution(arr1, arr2):
# #     answer = [] 
# #     for b in range(len(arr1)):
# #         answer.append([])
# #     for i in range(len(arr1)):
# #         for a in range(len(arr2)):
# #             answer[i].insert(a, (arr1[i][a]+arr2[i][a]))
        
# #     return answer
# # solution(3, 4)

# # #for i in range():
# # # (3) 0-2 1 씩 증가 
# # # (0, 3) 0-2 1씩 증가
# # # (3, 0, -1) 3-1  -1씩 감소   


# def solution(s):
#     answer = ''
#     a = 0
    
#     while(len(answer)!=len(s)):
#         for i in range(len(s)-1, 0, -1):
#             if(s[i]<s[i-1]):
#                 answer = answer + s[i]
#                 answer = answer - s[i]
            
#     return answer

# l= list("program")
# print(''.join(l)) -> convert list to string
# print(list("program")) -> convert string to list
# string is sort/reverse/+/- ---able 
# # print(solution("Zbcdefg"))


# def solution(s):
#     answer = ''
#     a = 0
#     lisw = (''.join(s))
#     print(lisw())
#     lisw.sort()
#     answer = lisw()
            
#     return answer

# print(solution("Zbcdefg"))

# s = "try hello world"
# answer = s
# answer = answer.split() # [Try, Hello, World]
# j = ""
# cap = ""
# pre = ""
# sm = ""
# d = ""
# for i in range(len(answer)): #0, 1, 2
#     j = answer[i] #1st: j = "Try" 2nd: j = "Hello"
#     for h in range(0, len(j)): #0, 2 / 0, 2, 4
#         if(h%2==0):
#             d = j[h].upper() #1st: "TrY" #j = j.replace(j[h], cap[h])
#             print(d)
#             print(h)
#             print(j)
#             if(len(sm)==len(s)):
#                 break
#             sm = sm + d
#         else:
#             sm = sm + j[h]
#         print(sm)
#         if(h==len(j)-1):
#                 sm = sm + " "
# answer = sm
# print(answer)

# s = "try   hello   world" #공백 3개씩
# answer = s.lower()#len(s)-
# answer = answer.split() # [Try, Hello, World]
# j = ""
# cap = ""
# pre = ""
# sm = ""
# d = ""
# for i in range(len(answer)): #0, 1, 2
#     j = answer[i] #1st: j = "Try" 2nd: j = "Hello"
#     for h in range(0, len(j)): #0, 2 / 0, 2, 4
#         if(h%2==0):
#             d = j[h].upper() #1st: "TrY" #j = j.replace(j[h], cap[h])
#             if(len(sm)==len(s)):
#                 break
#             sm = sm + d
#         else:
#             sm = sm + j[h]
#         if((h==len(j)-1) and (j!=answer[len(answer)-1])):
#                 sm = sm + " "
# answer = sm
# print(answer)

# s = "try   hello   world" #공백 3개씩
# answer = s.lower()
# # answer = answer.split() # [Try, Hello, World]
# j = ""
# cap = ""
# pre = ""
# sm = ""
# d = ""

# for i in range(len(answer)): #0, 1, 2, 3...17, 18
#     #j = answer[i] #1st: j = "Try" 2nd: j = "Hello"
#     if(answer[i] == ""):
#         sm = sm + ""
#     #for h in range(0, len(j)): #0, 2 / 0, 2, 4
#     if(i%2==0):
#         d = answer[i].upper() #1st: "TrY" #j = j.replace(j[h], cap[h])
#         sm = sm + d
#     else:
#         sm = sm + answer[i]
#     if(len(sm)==len(s)):
#         break
    
# answer = sm
# print(answer)


# n = 102940
# answer = []
# m = 1
# r = n
    
# while(r!=0):
#     m = r%10 # 1000%10=0
#     print(m) #0
#     if(r==0):
#         break
#     answer.append(m) #[-2]
#     print(answer)
#     r = int((r)/10) #-3452+2=-3450/10 = -345
#     print(r)

# if(n==0):
#     answer.append(n)

# print(answer)
'''

def solution(s):
    if((len(s)==4) or (len(s)==6)):
        try:
            s/2
        except nameoferror as answer:
            answer = False
        else:
            answer = True
    else:
        answer = False
       
    return answer



dic = {"name":"Jacq"}
dic["age"] = 20
dic["name"] = "Jeff"
'''
# s = "one4seveneight"
# num = ''
# leng = 0
# lis = []
# answer = 0
# ten = 1
# d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

# for i in range(len(s)):
#     num = num + s[i]
#     print(num)
#     for j in range(len(d)):
#         if((num==d[j]) or (num==j)):
#             lis.append(j)
#             print(lis)
#             leng += 1
#             num = ''
#         print(lis)
# lis.reverse()
# for o in range(leng):
#     for h in range(leng):
#         ten = ten * 10
#     answer = answer + (lis[o]*ten)
#     leng -= 1
    

s = "one4seveneight"
num = ''
lis = []
answer = 0
d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

for i in range(len(s)):
    num = num + s[i]
    print(num)
    if num in d:
        lis.append(d[num])
        print(lis)
        num = ''
    else:
        try:
            int(num)
        except:
            num = num
        else:
            lis.append(int(num))
            print(lis)
            num = ''
for h in range(len(lis)):
    answer = (answer + lis[h])*10
answer = int(answer/10)