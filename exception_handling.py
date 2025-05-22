''''''
'''
NameError 
'''
# a=10
# print(b)
# NameError: name 'b' is not defined
'''
ValueError
'''
# s='hello'
# print(s.index('p'))
#ValueError: substring not found
# lst=[1,2,3,4]
# lst.remove(11)
#ValueError: list.remove(x): x not in list
'''
TypeError
'''
# s='hi'
# s.upper(1)
#TypeError: str.upper() takes no arguments (1 given)
# s=10
# s[1]
#TypeError: 'int' object is not subscriptable

# lst=[1,2,3,4]
# lst.extend(10)
#TypeError: 'int' object is not iterable
'''
AttributeError
'''
# s='hello'
# s.append('l')
#AttributeError: 'str' object has no attribute 'append'
# lst=[1,2,3]
# lst.upper()
#AttributeError: 'list' object has no attribute 'upper'
'''
IndexError
'''
# lst=[1,2,3,4,5]
# lst[100]
#IndexError: list index out of range
# lst.pop(100)  #IndexError: pop index out of range
'''
KeyError
'''
# dic={'a':1,'b':2,'c':3}
# dic['d']
#KeyError: 'd'
# s={1,2,3,4}
# s.remove(10)
#KeyError: 10

'''
SyntaxError
'''
# s='hello's
# print(s)
#SyntaxError: unterminated string literal (detected at line 62)
# no=10
# if no > 9
#     print('hello')
#SyntaxError: expected ':'
'''
IndentationError
'''
 # a=10
# IndentationError: unexpected indent
'''
ZeroDivisionError
'''
# print(10/0)
#ZeroDivisionError: division by zero





'''
try:  
                        #here we will write the code which is having error
    statement
except:
                        #it will get exicuted if the try block having error
    statement
else:
                        #it will get exicuted if the try block won't have any error
    statement
finally:
                        #it will get exicuted mandatory 
    statememt
'''
# a=10
# lst=[1,2,3]
# try:
#     # print(b)  #NameError
#     # lst.upper()  #AttributeError
#     lst.pop(1000)  #IndexError
# except:
#     print('error')
# else:
#     print('no error')
# finally:
#     print('i will exicute mandatory')
'''
error
i will exicute mandatory
'''


'''
try:
    statement
except(Exception_name):
    statement
else:
    statement
finally:
    statement
'''
# s='hello'
# try:
#     # print(s[100]) #IndexError
#     s.pop()   #AttributeError
# except(IndexError):
#     print('error')
# else:
#     print('no error')
# finally:
#     print('i am a finally block')

'''
AttributeError: 'str' object has no attribute 'pop'
i am a finally block
'''
'''
try:
    statement
except(Exception_name1,Exception_name2,.....):
    statement
else:
    statement
finally:
    statement
'''
# lst=[1,2,3,4,5]
# try:
#     print(lst.upper(100))   #IndexError
# except (NameError,AttributeError,IndexError) as msg :
#     print('error')

'''
try:
    statement
except(Exception_name):
    statement
except(Exception_name):
    statement
except(Exception_name):
    statement
.
.
else:
    statement
finally:
    statement
'''
# a='hello'
# try:
#     print(21/0)
# except(NameError) as msg:
#     print(f'NAME ERROR:{msg}')
# except(IndexError) as msg:
#     print(f'INDEX ERROR:{msg}')
# except(ZeroDivisionError) as msg:
#     print(f'ZERO DIVISION ERROR:{msg}')


# class AgeError(Exception):
#     pass
# age=int(input('enter the age:'))
# if age >=18:
#     print('eligible')
# else:
#     raise AgeError('you are not eligible')

# '''
# BANK
# withdraw
# 1.ZeroBalanceError : if the account is having 0 ruppes
# 2.InsufficientBalanceError: if user ask more money than existing one
# '''
# class ZeroBalanceError(Exception):
#     pass
# class InsufficientBalanceError(Exception):
#     pass
# balance=100
# amt=int(input('enter the amount:'))  #150
# if balance >0:
#    if amt <=balance:
#         print(f'withdraw of {amt} is sucesfull')
#    else:
#        raise InsufficientBalanceError(f'you are lack of {amt-balance} RS')
# else:
#     raise ZeroBalanceError('you have 0 rs')

'''
TO MODIFY THE EXISTING ERROR MSG 
'''
# b=0
# if b==0:
#     raise ZeroDivisionError('you can not divide any number with zero')
