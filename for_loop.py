''''''
'''
syntax:
for variable_name in range/collection:
    stmt

range():
range([sv,]ev[,stepvalue])
-------
'''
#wap to print 1 to 10 numbers
# for i in range(1,11):
    # print(i,end=' ')
# 1 2 3 4 5 6 7 8 9 10
'''
wap to print 10 to 1 numbers
'''
# for i in range(10,0,-1):
#     print(i,end=' ')
# 10 9 8 7 6 5 4 3 2 1 2

'''
wap to traverse through a string 
'''
# s=input('enter the string:')
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1
#==================================
# s='hello'
# for i in range(len(s)):
#     # i -->> 0 1 2 3 4
#     print(s[i])
#===============================
# s='hello'
# for i in s:
#     print(i)

'''
wap to traverse through a list 
'''
# lst=['hello','apple','orange','mango']
# for i in range(len(lst)):
#     #i-->> 0 1 2 3
#     print(lst[i])
#-=-=================================
# for i in lst:
    #i--hello ,apple,orange,mango
    # print(i)
'''
wap to traverse through a dictionary 
'''
# dic={'a':1,'b':2,'c':3}
# for i in dic:
#     #it will gives the keys
#     print(i)
#     print(dic[i])
'''
a
b
c
'''
# dic={'a':1,'b':2,'c':3}
# for i in dic.values():
#     #it will gives the keys
#     print(i)
'''
1
2
3
'''

# dic={'a':1,'b':2,'c':3}
# for i in dic.items():  #[(),()]
#     #it will gives the keys
#     print(i)
'''
('a', 1)
('b', 2)
('c', 3)
'''
'''
wap to create a new list from the existing list
'''
# lst=['apple','orange','mango','facebook']
# res=[]
# for i in range(len(lst)):
#     ele=lst[i]
#     res.append(ele)
# print(res)
#==============================
# for i in lst:
    #i-- apple
    # res.append(i)
# print(res)
# ['apple', 'orange', 'mango', 'facebook']

'''
wap to create a list from a string if the element is present in even index
'''
# s='hello'
#o/p:['h','l','o']
# res=[]
# for i in range(len(s)):
#     if i%2==0:
#         ele=s[i]
#         res.append(ele)
# print(res)

'''
wap to create a dictionary from a string with key as element
 and value as opposite  case of the element
'''
s='HeLlO'
#o/p:--> {'H':'h','e':'E',L:l,l:L,O:o}
# dic={}
# for i in s:
#     if i.isupper():
#         key=i
#         val=i.lower()
#         dic[key]=val
#     else:
#         key=i
#         val=i.upper()
#         dic[key]=val
# print(dic)
'''
wap to create a dictionary from a list with key as element and 
value as reversed element
'''
# lst=['qspiders','facebook','twitter','whatsapp']
# dic={}
# for i in lst:
#     i--> qspiders
    # key=i
    # val=i[::-1]
    # dic[key]=val
# print(dic)
'''
{'qspiders': 'sredipsq', 'facebook': 'koobecaf', 
'twitter': 'rettiwt', 'whatsapp': 'ppastahw'}
'''



'''
1.wap to create a list from the existing list
if the elements present in the list starting with uppercase
'''
# lst=['Apple','bannana','Grapes','Qspiders','jspiders']
# res=[]
# for i in lst:
#     if i[0].isupper():
#         res.append(i)
# print(res)
'''
2.wap to create a dictionary from a list
with key as first_half_of the element and value as second_half_of the element
if the element is having even length
else  element and length pair
'''
# lst=['apple','orange','bannana','qspiders','facebook']
# dic={}
# for i in lst:
#     if len(i) % 2==0:
#         key=i[:len(i)//2]
#         val=i[len(i)//2:]
#         dic[key]=val
#     else:
#         key=i
#         val=len(i)
#         dic[key]=val
# print(dic)

'''
wap to create a dictionary from 2 lists 
with key from first list and value from second list with a hike of 15 % 
'''
# name=['dinga','dingi','manga','mangi']
# sal=[1000,2000,3000,4000]
# dic={}
# for i in range(len(name)):
#     i--> 0 1 2  3
    # key =name[i]
    # val=sal[i]+sal[i]*15//100
    # dic[key]=val
# print(dic)
'''
{'dinga': 1150, 'dingi': 2300, 'manga': 3450, 'mangi': 4600}
'''
'''
loop control statements
'''
# lst=[1,2,3,4,55,6,7,8]
# for i in lst:
#     if i>9:
#         break
#     else:
#         print(i)
'''
1
2
3
4
'''

# lst=[1,2,3,4,55,6,7,8,9]
# for i in lst:
#     if i>9:
#         continue
#     else:
#         print(i)
'''
1
2
3
4
6
7
8
9
'''
# age=19
# if age>=18:
#     pass
# else:
#     print('invalid')

'''
PRIME NUMBER
'''
# no=6
# a=True  # assume it is a prime
# for i in range(2,no):
#     if no%i==0:
#         a=False  #change the decision to false
#         break
# if a==True:
#     print('prime')
# else:
#     print('not a prime')


# no=7
# for i in range(2,no):
#     if no%i==0:
#         print('not a prime')
#         break
# else:
#     print('prime')

'''
wap to create a dictionary from a string and a list
with key from a string and values from a list
'''
# s='hello'
# lst=[1,2,3,4,5]
# dic={}
# for i in range(len(s)):
#     i -->> 0 1 2 3 4
    #indexing
    # key=s[i]
    # val=lst[i]
    # dic[key]=val
# print(dic)
#{'h': 1, 'e': 2, 'l': 4, 'o': 5}

'''
wap to check whether given list is homogeneous or not 
'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# a=True  #homo
# for i in lst:
#     #i --->> 1 2 3.3 4 5 6 7 8 9 10
#     if type(lst[0])==type(i):
#         pass
#     else:
#        a=False
#        break
# if a==True:
#     print('homo')
# else:
#     print('hetro')

# lst=[1,2,3,4]
# for i in lst:
#     if type(lst[0])!=type(i):
#         print('hetro')
#         break
# else:
#     print('homo')

'''
wap to seperate fruits flowers and plants 
'''
# lst=['rose flower','neem plant','jasmine flower','apple fruit','tulasi plant','orange fruit']
# dic={}
# for i in lst:
#     val,key=i.split()
#     if key not in dic:
#         dic[key]=[val]
#     else:
#         dic[key]=dic[key]+[val]
        # dic[key].append(val)
# print(dic)
'''
{'flower': ['rose', 'jasmine'], 'plant': ['neem', 'tulasi'], 'fruit': ['apple', 'orange']}
'''



'''
wap to get input from a user
'''
# lst=[]
# print('ENTER STOP ONCE DONE')
# while True:
#     element=input('enter the element:')
#     if element.lower()=='stop':
#         break
#     else:
#         lst.append(eval(element))
# t=tuple(lst)
# print(t)












