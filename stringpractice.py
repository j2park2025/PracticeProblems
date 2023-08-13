# ######연습문제1######
# s = "<html><body>Python</body><html>"
# stind = s.lstrip('<html><body>')
# stind = stind.rstrip('</body><html>')
# print(stind)

# ######연습문제2######
# def solution(s):
#     vc1 = s.count('a')
#     vc5 = s.count('A')
#     vc6 = s.count('e')
#     vc7 = s.count('U')
#     vc8 = s.count('u')
#     vc9 = s.count('I')
#     vc10 = s.count('i')
#     vc2 = s.count('E')
#     vc3 = s.count('O')
#     vc4 = s.count('o')
#     finalcount = vc1 + vc2 + vc3 + vc4 + vc5 + vc6 + vc7 + vc8 + vc9 + vc10
#     print("모음의 개수:", finalcount)

# print(solution("TONY'S CODING"))

# ######연습문제3######
# def solutionere():
#     print("********* 회원가입 *********")
#     Name = str(input("Name: "))
#     Birth = str(input("Birthday: "))
#     Phone = str(input("Phone Number: "))호

#     Birth_ed = Birth.replace(Birth[5:7], "**")
#     Birth_ed = Birth_ed.replace(Birth_ed[8:10], "**")

#     Phone_ed = Phone.replace(Phone[4:8], "****")
#     Phone_ed = Phone_ed.replace(Phone_ed[9:12], "***")
#     print("이름은 ", Name)
#     print("생년월일은 ", Birth_ed)
#     print("핸드폰 번호는 ", Phone_ed)

# solutionere()

######연습문제4######
# def solutionary():
#     Acl = "Kim Lee Park Choi Lee"
#     Bcl = "Kim Kim Jang Lim Lee"
    
#     inp1 = str(input("원하는 반: "))
#     inp2 = str(input("원하는 정보(학급 번호/명수): "))
#     inp3 = str(input("원하는 이름(Kim, Lee, etc.): "))

#     if((inp1=='A') and (inp2=='학급 번호')):
#         Aclis = Acl.split(' ')
#         astuloc = Aclis.index(inp3)
#         print(inp1, "반의", inp3, "학생은", astuloc, "번 입니다")
#     if((inp1=='A') and (inp2=='명수')):
#         astunumb = Acl.count(inp3)
#         print(inp1, "반의", inp3, "학생은", astunumb, "명 입니다")
#     if((inp1=='B') and (inp2=='학급 번호')):
#         Bclis = Bcl.split(' ')
#         bstuloc = Bclis.index(inp3)
#         print(inp1, "반의", inp3, "학생은", bstuloc, "번 입니다")
#     if((inp1=='B') and (inp2=='명수')):
#         bstunumb = Bcl.count(inp3)
#         print(inp1, "반의", inp3, "학생은", bstunumb, "명 입니다")
#     if((inp1==('A,B')) and (inp2=='명수')):
#         bstunumb = Bcl.count(inp3)
#         astunumb = Acl.count(inp3)
#         print(inp1, "반의", inp3, "학생은", astunumb + bstunumb, "명 입니다")

#     Aclrep = Acl.replace(' ', ',')
#     Bclrep = Bcl.replace(' ', ',')

#     print(Aclrep)
#     print(Bclrep)

# print(solutionary())

# ######연습문제5######
# s = "!@?!////!python!@?!////!"
# stind = s.strip('!@?!////!')
# print(stind)

# ######연습문제6######
# name = "김나연 김다슬 박수현 이하나 이하나"
# num = "1 2 3 4 5"
# namesp = name.split()
# for i in range(1, len(namesp)+1):
#     print("학생 #", i, "id : ", namesp[i-1], i)

# ######연습문제7######
# a = str(input("name?"))
# print("Dear", a, ",")
# print("Can you join the class today?")
# print("")
# print("Sincerely,")
# print("Tony's Coding")

# ######연습문제8######
# s1 = "Hello! Tony's Coding"
# s2 = "This is"
# sli1 = s1.split()
# s3 = sli1[0] + " " + s2 + " " + sli1[1] + " " + sli1[2]
# print(s3)

# ######도전문제1######
# mes = str(input("메세지를 입력하시오:"))
# result = ""
# result = mes.title()
# result = result.swapcase()
# print("메세지 암호화: ", result)

######도전문제2######
dia = str(input("문자열:"))
diali = dia.split() # ["사과", "딸기", "포도"]
st = ""
answer = ""
smap = ""
smap = diali[0]
for k in range(len(smap)):
    for i in range(len(diali)):
        st = diali[i]
        for h in range(len(st)-1):
            if(len(answer)==len(diali)):
                answer = answer + " "
            answer = answer + st[k]
        if(len(answer)==(len(st)*len(diali))+(len(diali)-1)):
            break
print("문자열 암호화:", answer)