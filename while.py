''''''
from itertools import count

'''
variable_name=value   looping variable declaration
while condition:
    code
    updation(increment/decrement)
'''
'''
wap to print hello python for 5 time's
'''
# i=1
# while i<6:
#     print('hello python')
#     i=i+1
'''
hello python
hello python
hello python
hello python
hello python
'''

'''
wap to print 1 to 10 numbers
o/p:-- 1 2 3 4 5 6 7 8 9 10
'''
# i=1
# while i<=10:
#     print(i,end=' ')
#     i+=1
# 1 2 3 4 5 6 7 8 9 10

'''
wap to print 10 to 1 numbers
o/p:- 10 9 8 7 6 5 4 3 2 1 
'''
# i=10
# while i>0:
#     print(i,end=' ')
#     i-=1

'''
wap to print even numbers from 1 to 10 
'''
# i=1
# while i <=10:
#     if i % 2==0:
#         print(i)
#     i=i+1
# ==================
# i=2
# while i<=10:
#     print(i)
#     i=i+2

'''
wap to print odd numbers from 1 to 10 
'''
# i=1
# while i<=10:
#     if i%2 !=0:
#         print(i)
#     i+=1
# -----------------------------------------------
# i=1
# while i<=10:
#     print(i)
#     i+=2

# wap to find the factorial of a given number

# no=int(input('enter the value'))
# fact=1
# while no>=1:
#     fact=fact*no
#     no=no-1
# print(fact)
'''
enter the value5
120
'''
'''
wap to reverse a given number
'''
# no=1234
# rev=0
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
#     no=no//10
# print(rev)
'''
wap to  check whether given number is palindrome or not
'''
# no=121
# rev=0
# temp=no
# while no>0:
#     rem=no%10
#     rev=rev*10+rem
#     no=no//10
# if rev==temp:
#     print('palindrome')
# else:
#     print('not a palindrome')

'''
wap to find sum of all the digits present in a given number
i/p: 1234
o/p:10
'''

# no=1234
# sum=0
# while no>0:
#     rem=no%10
#     sum=sum+rem
#     no=no//10
# print(sum)
'''
wap to find no of digits present in a given number
'''
# no=1234
# count=0
# while no>0:
#     count +=1
#     no=no//10
# print(count)

'''
wap to check whether given number is amstrong number or not 
'''
# no=153
# temp=no
# temp1=no
# count=0
# sum=0
# while no>0:
#     count+=1
#     no=no//10
# while temp>0:
#     rem=temp%10
#     sum+=rem**count
#     temp=temp//10
# if sum==temp1:
#     print('AMSTRONG NUMBER')
# else:
#     print('NOT A AMSTRONG NUMBER')

# no=153
# temp=no
# count=len(str(no))
# sum=0
# while no>0:
#     rem=no%10
#     sum+=rem**count
#     no=no//10
# if temp==sum:
#     print('AMSTRONG NUMBER')
# else:
#     print('NOT A AMSTRONG NUMBER')
'''
FIBONACCI SERIES
'''
# no=int(input('enter number of values you want to display:'))
# a=0
# b=1
# print(a,b,end=' ')
# count=1
# while count<=no-2:
#     c=a+b
#     a=b
#     b=c
#     count+=1
#     print(c,end=' ')
'''
enter number of values you want to display:10
0 1 1 2 3 5 8 13 21 34 
'''
'''
PERFECT NUMBER
'''
# no=6
# sum=0
# i=1
# while i <no:
#     if no %i==0:
#         sum+=i
#     i+=1
# if sum==no:
#     print('perfect number')
# else:
#     print('not a perfect number')
'''
PERFECT SQUARE
'''
# no=25
# temp=no**0.5
# if temp==int(temp):
#     print('perfect square')
# else:
#     print('not a perfect square')
'''
STRONG NUMBER
'''
# no=145
# temp=no
# sum=0
# while no>0:
#     rem=no%10
#     fact=1
#     while rem>0:
#         fact=fact*rem
#         rem=rem-1
#     sum+=fact
#     no=no//10
# if temp==sum:
#     print('strong  number')
# else:
#     print('not a strong number')
'''
xylem and pholem number
'''
# no=1234
# temp=no
# o_sum=0
# i_sum=0
# while no>0:
#     rem=no%10
#     if no==temp or no <10:
#         o_sum+=rem
#     else:
#         i_sum+=rem
#     no=no//10
# if o_sum==i_sum:
#     print('xylem number')
# else:
#     print('pholem number')

'''
HAPPY NUMBER
'''
# no=13
# while no>9:
#     sum=0
#     while no>0:
#         rem=no%10
#         sum+=rem**2
#         no=no//10
#     no=sum
# if no==1 :
#     print('happy number')
# else:
#     print('not a happy number')

'''
HARSHAD OR NIVEN NUMBER
'''
# no=24
# sum=0
# temp=no
# while no >0:
#     rem=no%10
#     sum+=rem
#     no=no//10
# if temp % sum==0:
#     print('HARSHAD NUMBER')
# else:
#     print('not a harshad number')

'''
number programs
--------------------------------------
1.number reverse
2.number palindrome
3.factorial of a number
4.sum of all the digits 
5.no of digits present in a number
6.armstrong
7.strong
8.fibonacci
9.perfect square
10.perfect number
11.xylem pholem
12.happy number
13.harshad number
**14.prime number**
'''
'''
FIRST 10 EVEN FIBONACCI NUMBERS
'''
# a=0
# b=1
# count=0
# while count<10:
#     c=a+b
#     if c%2==0:
#         print(c,end=' ')
#         count+=1
#     a=b
#     b=c
'''
2 8 34 144 610 2584 10946 46368 196418 832040 
'''

'''
wap to traverse through a string 
'''
# s='qspiders'
# i=0
# while i<len(s):
#     print(s[i])
#     i+=1
'''
q
s
p
i
d
e
r
s
'''
'''
wap to create a new string from the old one by converting
 uppercase letters into lower and lower case letters into upper
'''
# s='HeLlO'
# res=''
# i=0
# while i<len(s):
#    if s[i].isupper():
#        ch=s[i].lower()
#        res=res+ch
#    else:
#        ch=s[i].upper()
#        res=res+ch
#    i+=1
# print(res)



























