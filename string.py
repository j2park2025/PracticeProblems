
######s.function()######
'''
s = "Hello World"
s.function_name()
'''

######s.count()######
s = "stuff as gssss krrf"
s_count = s.count('s')
print("s의 개수:", s_count)
print()

######s.find()######
o_find = s.find('o')
g_find = s.find('g')
print("o의 위치는", o_find)
print("g는", g_find) 
print()
#returns -1 if theres no g in the text

######s.index()######
s = "do you like coding?"
d_index = s.index('d')
i_index = s.index('i')
ques_index = s.index('?')
e_index = s.index('e')
print("d, i, ?, e의 위치 순서대로:", d_index, i_index, ques_index, e_index)
print()
#없으면 오류남

######s.join()######
s = "abcd"
s_join = ",".join(s)
print("s :", s)
print("',' 문자삽입 :", s_join)
print()

######s.upper()######
s = "Tony's coding"
s_upper = s.upper()
print("\t s         :", s)
print("\t s.upper() :", s_upper)
print()

######s.lower()######
s = "TOnY's CoDIng"
s_lower = s.lower()
print("\t s         :", s)
print("\t s.lower() :", s_lower)
print()

######s.lstrip()######
s = "        Hi        "
s_lstrip = s.lstrip()#여기 bracket 안에 빈거는 그냥 space 지우는거 여기에 만약에 앞에 .....가 있으면 점 찍으면 됨
print("s               :", s)
print("s 길이          :", len(s))
print("s.lstrip()      :", s_lstrip)
print("s.lstrip() 길이 :", len(s_lstrip))
print()

######s.rstrip()######
s = "        Hi        "
s_rstrip = s.rstrip()#여기 bracket 안에 빈거는 그냥 space 지우는거 여기에 만약에 뒤에 .....가 있으면 점 찍으면 됨
print("s               :", s)
print("s 길이          :", len(s))
print("s.rstrip()      :", s_rstrip)
print("s.rstrip() 길이 :", len(s_rstrip))
print()

######s.strip()######
s = "        Hi        "
s_strip = s.strip()#여기 bracket 안에 빈거는 그냥 space 지우는거 여기에 만약에 양쪽에 .....가 있으면 점 찍으면 됨
print("s               :", s)
print("s 길이          :", len(s))
print("s.strip()       :", s_strip)
print("s.strip() 길이  :", len(s_strip))
print()

######s.replace()######
s = "Hello World"
s_rep = s.replace("Hello", "Bye")
print("s: ", s)
print("s.replace(): ", s_rep)
print()

s_rep = s_rep.replace("World", "Everyone")
print("s: ", s)
print("s.replace(): ", s_rep)
print()

######s.split()######
s = "Python is Fun"
s_sp = s.split()#여기에다가 또 같이 :, *, (, &, ^뭐 이런거 ',' 해가지고 넣으면 이거에 따라서 분리+리스트에 입력
print("s: ", s)
print("type(s): ", type(s))
print("length of s: ", len(s))
print() #enter
print("s.split(): ", s_sp)
print("type(s_sp): ", type(s_sp))
print("length of s_sp: ", len(s_sp))



