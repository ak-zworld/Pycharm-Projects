''''''
'''
1.type()
-->> it is used to return what type of data we are storing in a particular variable
'''
# a=10
# print(type(a))

'''
2.id()
--->> it is used to return object address of an variable
'''
# a='hello'
# print(id(a))
'''
3.round()
--->> it is used to round off the given number into a nearest integer
'''
# a=10.6
# print(round(a)) 11
# print(round(10.3))   10

'''
4.chr()
-->> it return the character based on the ascii value
'''
# print(chr(97))   a
'''
5.ord()
-->>> it accept the character and return's the ascii value of that character
'''
# print(ord('t'))    116

'''
6.divmod()
-->> it is used to return division and modulues of a given number
'''
# print(divmod(4,2))     (2,0)
'''
7.abs()
--->> it is used to remove the symbols from an expression
'''
# print(abs(-10))   10

# '''
# 8.enumerate()
# ----------
# collection:--->> gives only elements
# range :---->> gives only index
# enumerate :--> gives both element and index
# '''
# lst=['hello','hi','good']
# for i in range(len(lst)):
#     print((i,lst[i]))
# '''
# (0, 'hello')
# (1, 'hi')
# (2, 'good')
# '''
# for i,j in enumerate(lst):
#     print(i,j)
# '''
# 0 hello
# 1 hi
# 2 good
# '''
'''
wap to create a dictionary from a list with key as first half and value as
second half in a reverse order if the index of the element is even 
else key will be first half in reverse order and value will be second half 
'''
# lst=['apple','orange','mango','qspiders','jspiders','tamarind']
# dic={}
# for i in range(len(lst)):
# #     0 1 2 3 4 5
#     if i %2==0:
#         key=lst[i][:len(lst[i])//2]
#         val=lst[i][len(lst[i])//2:][::-1]
#         dic[key]=val
#     else:
#         key = lst[i][:len(lst[i]) // 2][::-1]
#         val = lst[i][len(lst[i]) // 2:]
#         dic[key]=val
# print(dic)

# for i,j in enumerate(lst):
#     i--->> index     j--- element
    # if i %2==0:
    #     key=j[:len(j)//2]
    #     val=j[len(j)//2:][::-1]
    #     dic[key]=val
    # else:
    #     key = j[:len(j) // 2][::-1]
    #     val = j[len(j) // 2:]
    #     dic[key] = val
# print(dic)
'''
wap to create a list from a string  if the elements index is divisible by 2
'''
# s='hello'
# lst=[]
# for i,j in enumerate(s):
# #     i--->> index   j--->> elements
#     if i % 2==0:
#         lst.append(j)
# print(lst)




d = {"Fruits": ["Mango", "Apple", "Kivi", "Grapes", "Banana"],
     "Vegitables": ["Tomato", "Potato", "Onion", "Spinach", "Beans"],
     "Plants": ["Neem plant", "Money plant", "alovera plant", "Rose plant"],
     "Trees": ["Banian tree", "Coconut tree", "sandal wood tree"]}
# for i ,j in enumerate(d,start=1):
#      #i___>> integer    j--- keys
#      print(f'{i}. {j}')
#      for k,l in enumerate(d[j]):
#           #k--->> integer    l-- elements
#           #0 1 2 3 4 5
#           print(f'\t\t\t{chr(97+k)}.{l}')
'''
o/p:-
1. Fruits
       a.Mango
       b.Apple
       c.Kivi
       d.Grapes
       e.Banana
2. Vegitables
       a.Tomato
       b.Potato
       c.Onion
       d.Spinach
       e.Beans
3. Plants
       a.Neem
       b.Money plant
       c.alovera plant
       d.Rose plant
4. Trees
       a.Banian tree
       b.Coconut tree
       c.sandal wood tree
'''
'''
WAP TO CREATE A NEW LIST WITH THE PRODUCT OF THE ELEMENTS PRESENT IN THE SAME INDEX
'''
# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# res=[]
# for i in range(len(lst1)):
#      #i---> 0 1 2  3 4
#      ele=lst1[i]*lst2[i]
#      res.append(ele)
# print(res)

# for i,j in zip(lst1,lst2):
     # i=lst1     j= lst2
     # ele=i*j
     # res.append(ele)
# print(res)
#[6, 14, 24, 36, 50]


'''
wap to create 2 dictionaries from 3 lists 
key from first list and values from remaining lists
'''
# names=['dinga','dingi','manga','mangi']
# sal=[1000,2000,3000,4000]
# comm=[100,200,300,400]
# dic1={}
# dic2={}
# for i,j,z in zip(names,sal,comm):
#     #i----names    j---sal z---comm
#     key=i
#     dic1[key]=j
#     dic2[key]=z
# print(dic1)
# print(dic2)
'''
{'dinga': 1000, 'dingi': 2000, 'manga': 3000, 'mangi': 4000}
{'dinga': 100, 'dingi': 200, 'manga': 300, 'mangi': 400}
'''
# from itertools import zip_longest
  #zip_longest(iterable1,iterable2,...,[fillvalue=None])
# from itertools import zip_longest
# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9]
# for i,j in zip_longest(lst1,lst2):
#     print(i,j)
'''
1 6
2 7
3 8
4 9
5 None
'''
'''
wap to create a dictionary with name and salary pair if salarie is present give 10%hike 
else give 0 
'''
# from itertools import zip_longest
# names=['dinga','dingi','manga','mangi']
# sal=[1000,2000,3000]
# dic={}
# for i,j in zip_longest(names,sal,fillvalue=0):
#     # i---key     j--val
#     val=j+j*10//100  #0+0*10//100
#     dic[i]=val
# print(dic)

'''
wap to create a dictionary from a company and country pair
if country is not present  add "not specified" as value
'''
# from itertools import zip_longest
# company=['TATA','APPLE','TOYOTO','MERCEDIES']
# country=['india','usa','japan']
# dic={}
# for i,j in zip_longest(company,country,fillvalue='not specified'):
#     #i---key   j--val
#     dic[i]=j
# print(dic)

#pandas
#wap to display the marksheet
# install from python packages :---- pandas
# import pandas as pd
# name=['dinga','dingi','manga','mangi']
# tamil=[100,80,70,60]
# english=[70,50,67,80]
# dic={'NAME':name,'TAMIL_MARKS':tamil,'ENGLISH_MARKS':english}
# df=pd.DataFrame(dic)
# print(df)
'''
    NAME  TAMIL_MARKS  ENGLISH_MARKS
0  dinga          100             70
1  dingi           80             50
2  manga           70             67
3  mangi           60             80
'''
import calendar as c
# year=int(input('enter the year'))
# if c.isleap(year):
#      print('leap year')
# else:
#      print('not a leap year')







