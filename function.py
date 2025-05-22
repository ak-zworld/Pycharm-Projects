#waf to add 2 numbers
# def add(a,b):
#     print(a+b)
# add(3,4)


#waf to return the subtract of 2 numbers
# def sub(a,b):
#     c=a-b
#     return c
# print(sub(4,2))
#==============================================
# def demo(a,b):
#     print(' i am exicuting before the return')
#     return a,b
#     print('i am exicuting after the return')
# print(demo(1,2))
#  i am exicuting before the return
# (1, 2)
''''''
'''
waf to return True if the given number is even else return False
'''
# def even_odd(no):
#     if no % 2==0:
#         return True
#     else:
#         return False
# a=int(input('enter the number:'))
# print(even_odd(a))
'''
waf to return prime if the given number is prime number else not a prime
'''
# def is_prime(no):
#     for i in range(2,no):
#         if no %i==0:
#             return 'not a prime'
#     else:
#         return 'prime'
# print(is_prime(7))

# def is_prime(no):
#     for i in range(2,no):
#         if no%i==0:
#             break
#     else:
#         return no
# for i in range(1,101):
#     a=is_prime(i)
#     if a!=None:
#         print(a)

'''
def function_name(parameters):
    stmt1
    stmt2
    yield data1
    yield data2
    .
    .
function_name(arguments)
'''
'''
waf to return even numbers present in a list
'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# def even(a):
#     for i in a:
#         if i%2==0:
#             yield i
# print(list(even(lst)))
'''
[2, 4, 6, 8, 10]
'''
'''
waf to return prime numbers from 1 to 1000
'''
# def is_prime():
#     for i in range(1,1001):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             yield i
#
# print(list(is_prime()))
'''
waf to return the elements which are starting with uppercase characters
'''
# lst=['Apple','qspiders','Jspiders','mango']
# def u_elements(a):
#     for i in a:
#         if i[0].isupper():
#             yield i
# print(list(u_elements(lst)))

'''
waf to return square and cube of a number
'''
# def sq_cu(no):
#     yield no ** 2
#     yield no ** 3
# print(list(sq_cu(2)))
'''
[4,8]
'''


'''
TYPES OF ARGUMENTS
------------------------
1.positional arguments
'''
# def demo(a,b,c,d):
#     print(a,b,c,d)
# demo(1,2,3,4)
'''
2.keyword arguments
'''
# def demo(a,b,c,d):
#     print(a,b,c,d)
# demo(b=2,d=4,a=1,c=3)
'''
3.combination of positional and keyword arguments
--> always positional arguments should be first followed by keyword arguments
'''
# def sample(a,b,c,d,e,f,g):
#     print(a,b,c,d,e,f,g)
# sample(1,2,3,4,5,6,7)
# sample(a=1,b=2,c=3,d=4,e=5,f=6,g=7)
# sample(1,2,3,d=4,e=5,f=6,g=7)
# sample(a=1,b=2,c=3,4,5,6,7)
# SyntaxError: positional argument follows keyword argument
# sample(1,2,3,4,5,a=6,g=7)
# sample() got multiple values for argument 'a'

'''
4.only positional arguments (/)
'''
# def demo(a,b,c,d,e,/):
#     print(a,b,c,d,e)
# demo(1,2,3,4,5)
# demo(a=1,b=2,c=3,d=4,e=5)  o/p: 1 2  3 4 5

# TypeError: demo() got some positional-only arguments passed as keyword arguments:'a, b, c, d, e'
# demo(1,2,c=3,d=4,e=5)
# TypeError: demo() got some positional-only arguments passed as keyword arguments:'c, d, e'
'''
5.only keyword arguments(*)
'''
# def demo(*,a,b,c,d):
#     print(a,b,c,d)
# demo(1,2,3,4)
# TypeError: demo() takes 0 positional arguments but 4 were given
# demo(a=1,b=2,c=3,d=4)
# demo(1,2,c=3,d=4)
# TypeError: demo() takes 0 positional arguments
# but 2 positional arguments (and 2 keyword-only arguments) were given
'''
6.combination of only positional and only keyword arguments
'''
# def sample(a,b,/,*,c,d,e):
#     print(a,b,c,d,e)
# sample(1,2,c=3,d=4,e=5)
# sample(1,2,3,d=4,e=5)
# TypeError: sample() takes 2 positional arguments but
# 3 positional arguments (and 2 keyword-only arguments) were given
'''
variable positional arguments(*args)
'''
# def add(*args):
    # print(*args)  it return the values with out any packing 1 2 3 4 5 6 7 8 9 10
    # print(args)  it return the values by packing into a tuple (1,2,3,4,5,6,7,8,9,10)
# add(1,2,3,4,5,6,7,8,9,10)
# add(1,2,3,4,5,6,a=7)
# TypeError: add() got an unexpected keyword argument 'a'
'''
waf to add the numbers 
'''
# def add(*args):
#     # sum=0
#     # for i in args:
#     #    sum+=i
#     # print(sum)
#     # ---------------------------
#     print(sum(args))
# add(1,2,3,4,5,6,7,8,9,10)
'''
variable keyword arguments(**kwargs)
'''
# def add(**kwargs):
    # print(**kwargs)   TypeError: 'a' is an invalid keyword argument for print()
    # print(*kwargs) --> it return's the keys with out any boundaries  a b c d e
    # print(kwargs) --> it return a dictionary{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# add(a=1,b=2,c=3,d=4,e=5)
'''
waf to multiply the numbers by using n no. of keyword arguments
'''
# def mul(**kwargs):
    # m=1
    # for i in kwargs:
    #     # dic[key]
    #    m*=kwargs[i]
    # print(m)
    # ----------------------------------------
    # for i in kwargs.values():
    #     m*=i
    # print(m)
# mul(a=1,b=2,c=3,d=4,e=5)
'''
9.combination of variable positional and variable keyword arguments
'''
# def demo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# demo(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)
'''
waf to add the  numbers
'''
# def add(*args,**kwargs):
    # sum=0
    # for i in args:
    #     sum+=i
    # for j in kwargs.values():
    #     sum+=j
    # print(sum)
    # -------------------------------
    # print(sum(args)+sum(kwargs.values()))
# add(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)


'''
decorator

def decorator_name(variable_name):
    def inner(parameters):
        stmt
        variable_name(parameters)
    retun inner
@decorator_name
def function_name(parameters):
    stmt
function_name(arguments)

'''



# def outer(func):
#     def inner(a,b):
#         print('hey dinga you got :',end=' ')
#         func(a,b)
#     return inner
# @outer
# def add(a,b):
#     print(a+b)
# add(4,5)
# @outer
# def sub(a,b):
#     print(a-b)
# sub(4,2)
'''
hey dinga you got : 9
hey dinga you got : 2
'''

'''
wadf to print a msg before printing the sum of all the number's
'''
# def deco(func):
#     def inner(*args,**kwargs):
#         print('the sum of args and kwargs is:',end=' ')
#         func(*args,**kwargs)
#     return inner
# @deco
# def add(*args,**kwargs):
#     sum=0
#     for i in args:
#         sum+=i
#     for j in kwargs.values():
#         sum+=j
#     print(sum)
# add(1,2,3,4,5,a=6,b=7,c=8,d=9,e=10)
'''
wadf to make program to wait for 5 sec while 
checking the OTP which user entered
'''

from time import sleep
# import random
# otp=random.randint(1000,9999)
# print(otp)
# user_name = input('enter the user_name')
# ot = int(input('enter the otp'))
# def deco(func):
#     def inner():
#         print('verifying...')
#         sleep(5)
#         func()
#     return inner
# @deco
# def login():
#     # dinga
#     if user_name=='dinga':
#         if otp==ot:
#             print('login sucesfull')
#         else:
#             print('not sucesfull')
#     else:
#         print('not sucesfull')
# login()





'''
wadf to swap the numerator and denominator if the denominator is zero
else print the results as it is 
'''
# def deco(func):
#     def inner(a,b):
#        if b==0:
#            func(b,a)   #b=0 a=4
#        else:
#            func(a,b)
#     return inner
# @deco
# def div(a,b):
#     print(a//b)
# div(4,2)


# from time import sleep
# def deco(func):
#     def inner():
#         print('hello..')
#         sleep(3)
#         func()
#     return inner
# @deco function_name=deco(function_name)
# def wish():
#     print('good morning')
# wish()
# @deco
# def bye():
#     print('bye..')
# bye()

'''
parameterized decorator
def decorator_name(parameters)
    def outer(variable_name):
        def inner(parameters):
            stmt
            variable_name(parameters)
        return inner
    return outer
@decorator_name(value) FUNCTION_NAME =DECORATOR_NAME(VALUE)(FUNCTION_NAME)
def function_name(parameters):
    stmt
function_name(arguments)
'''
# from  time import sleep
# def is_sleep(n):
#     def outer(func):
#         def inner(a,b):
#             print('hello')
#             sleep(n)
#             func(a,b)
#         return inner
#     return outer
# @is_sleep(5)
# def add(a,b):
#     print(a+b)
# add(2,5)
# @is_sleep(2)
# def sub(a,b):
#     print(a-b)
# sub(4,2)

'''
wadf to execute the program for n no of times based on the user input
'''
# def execute(no):
#     def outer(func):
#         def inner():
#             for i in range(no):
#                 func()
#         return inner
#     return outer
# no=int(input('enter the number:'))
# @execute(no)
# def wish():
#     print('hello')
# wish()
# no=int(input('enter the number:'))
# @execute(no)
# def bye():
#     print('bye..')
# bye()

'''
scopes in python
1.global scope
2.local scope
3.non local scope
'''
# a=10  #global variable
# print(f'i am printing before the function {a}')    #10
# def demo():
#     global a
#     a=20   #global variable
#     print(f'i am printing inside the function {a}')  #20
# demo()
# print(f'i am printing after the function {a}')   #20
'''
i am printing before the function 10
i am printing inside the function 20
i am printing after the function 20
'''


'''
local variable
'''
# def sample():
#     b=100  #local variables
#     print(f'i am printing inside the function {b}')  #100
#     def demo():
#         nonlocal b
#         b=1
#         print(f'i am printing inside the nested function {b}')  #1
#     demo()
#     print(f'i am printing after  the nested function {b}') #1
# sample()
'''
i am printing inside the function 100
i am printing inside the nested function 1
i am printing after  the nested function 1
'''

'''
non local variable
'''
# def sample():
#     def demo():
#         c=30  #non local variable
#         print(c)
#     demo()
# sample()

# a=10  #global variable
# print(f'i am printing before the function {a}')  #10
# def sample():
#     global a
#     a=100
#     print(f'i am printing inside the function {a}')  #100
#     b=20   #local variable
#     print(f'i am printing inside the function {b}') #20
#     def demo():
#         global a
#         a=0
#         print(f'i am printing inside the nested  function {a}')  #0
#         nonlocal b
#         b=200
#         print(f'i am printing inside the nested function {b}') #200
#         c=30
#         print(f'i am printing inside the  nested function {c}')  #30
#     demo()
#     print(f'i am printing after the nested function {b}') #200
# sample()
# print(f'i am printing outside the function {a}')  #0
'''
i am printing before the function 10
i am printing inside the function 100
i am printing inside the function 20
i am printing inside the nested  function 0
i am printing inside the nested function 200
i am printing inside the  nested function 30
i am printing after the nested function 200
i am printing outside the function 0
'''
#lambda

'''
wap to return square of a given number
'''
# def sq(no):
#     return no**2
# print(sq(3))

# a=lambda no:no**2
# print(a(3))

'''
walf to add 2 numbers
'''
# def add(a,b):
#     return a+b
# print(add(3,4))
# ==========================
# add=lambda a,b:a+b
# print(add(3,4))
'''
walf to return length of an integer
'''
# def length(no):
#     return len(str(no))
# print(length(1234))
#==========================================
# length=lambda no:len(str(no))
# print(length(1234))

'''
walf to return the decimal values present in a number
ex: 10.234523
o/P: 234523
'''
# def decimal(no):
#     # a=str(no)         #'10.234567'
#     # b=a.split('.')    #['10','234567']
#     # c=int(b[1])       #234567
#     # return c
#     return int(str(no).split('.')[1])
# print(decimal(10.234567))
# ==================================================
# decimal=lambda no: int(str(no).split('.')[1])
# print(decimal(10.23456789))
'''
walf to reverse a string
'''
# rev=lambda s:s[::-1]
# print(rev('hello'))

'''
walf to return hello if the given number is even else return bye
'''
# def even_odd(no):
#     if no % 2==0:
#         return 'hello'
#     else:
#         return 'bye'
# print(even_odd(11))
'''
syntax:
lambda arg1,arg2: exp if condition else expression
'''
# even_odd=lambda no: 'hello'if no%2==0 else 'bye'
# print(even_odd(11))
'''
walf to reverse a string if it is having even length else return as it is 
'''
# even_length=lambda s: s[::-1]if len(s)%2==0 else s
# print(even_length('orange'))
'''
walf to create a dictionary from a list with key as index and value as element
'''
# lst=['hello','good','morning','bye']
# d=lambda a: dict(enumerate(a))
# print(d(lst))

'''
walf to return last n no of characters based on the user_input
s='programming'
4
ming
'''
# s='programming'
# no=int(input('enter no of characters:'))  #4
# ele=lambda value,number:value[-number:]
# print(ele(s,no))
#
#walf to return first n no of characters based on the user_input
# s='programming'
# no=int(input('enter no of characters:'))  #4
# ele=lambda value,number:value[:number]
# print(ele(s,no))


# def cub(no):
#     return no**3
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     print(cub(i))

# a=lambda no:no**3
# lst=[1,2,3,4,5,6,7,8,9]
# for i in lst:
#     print(a(i))
'''
map(function,itterable)
--->> it return map object address    1 8 27
'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# a=lambda no:no**3
# res=map(a,lst)
# print(list(res))
'''
1 8 27....
'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# def cub(no):
#     return no**3
# res=map(cub,lst)
# print(list(res))

'''
waf to return the sum of the elements present in 2 list at same index
'''
# lst1=[1,2,3]
# lst2=[4,5,6]
# def add(x,y):
#     return x+y
# for i,j in zip(lst1,lst2):
#     #i -- lst1     j -- lst2
#     print(add(i,j))

# add=lambda x,y:x+y
# for i,j in zip(lst1,lst2):
#     print(add(i,j))

# add=lambda x:x[0]+x[1]
# res=map(add,zip(lst1,lst2))   #(1,4) (2,5)
# print(list(res))

# add=lambda x,y:x+y
# res=map(add,lst1,lst2)
# print(list(res))
# lst1=[1,2,3]
# lst2=[4,5,6]
# def add(x,y):
#     return x+y
# res=map(add,lst1,lst2)
# print(list(res))

# def add(x):
#     return x[0]+x[1]
# res=map(add,zip(lst1,lst2))
# print(list(res))
'''
wamf to remove the spaces from the front and back of a string
'''
# lst=['   dinga   ','   hello  ','   python   ','   qspiders    ']
#o/p: ['dinga','hello','python','qspiders']
# def is_space(s):
#     return s.strip()
# for i in lst:
#     print(is_space(i))

# is_space=lambda s:s.strip()
# res=map(is_space,lst)
# print(list(res))
'''
wamf to return only the elements which are starting with vowel
'''
# lst=['apple','banana','orange','grapes']
# r=[]
# vow=lambda s: s if (s[0].lower() in'aeiou') else None
# res=map(vow,lst)   #apple   None  orange   None
# for i in res:
#     #i==None
#     if i !=None:
#         r.append(i)
# print(r)


'''
wa fiter function to return even numbers present in a list
'''
# lst=[1,2,3,4,5,6,7,8,9]
# even=lambda no:no%2==0
# res=filter(even,lst)
# print(list(res))

'''
waf to return square of all the even numbers present in a list
'''
# lst=[1,2,3,4,5,6,7,8,9,10]
# even=lambda no:no%2==0
# numbers=filter(even,lst)  #2 4 6 8 10
# sq=lambda e_no:e_no**2
# res=map(sq,numbers)
# print(list(res))
#================================
# print(list(map(lambda e_no:e_no**2,filter(lambda no:no%2==0,[1,2,3,4,5,6,7,8,9,10]))))










