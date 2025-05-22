''''''
'''
if condition:
 if condition:
     -------
    |  TSB |
    -------
 elif condition:
    -------
    |  TSB |
    -------
 else:
     -------
    |  FSB |
    -------
elif condition:
 if condition:
     -------
    |  TSB |
    -------
 elif condition:
    -------
    |  TSB |
    -------
 else:
     -------
    |  FSB |
    ------- 
else:
  if condition:
     -------
    |  TSB |
    -------
 elif condition:
    -------
    |  TSB |
    -------
 else:
     -------
    |  FSB |
    -------
'''
'''
wap to check whether given number is even or odd before checking check whether given number is 
positive or negative
'''
# no=int(input('enter the number:'))
# if no==0:
#     print('neutral number')
# elif no>0:
#     positive
#     if no%2==0:
#         print('positive even number')
#     else:
#         print('positive odd number')
# else:
#     negative
    # if no%2==0:
    #     print('negative even number')
    # else:
    #     print('negative odd number')




# print('\t\t\t\t\tWELCOME TO QSPIDERS RESTARENT')
# print('1.breakfast\n2.lunch\n3.dinner')
# option=int(input('enter the option:'))
# if option==1:
#     print('\t\tBREAKFAST MENU')
#     print(f'\t{'-'*23}')
#     print('1.idli-10RS\n2.Dosa-40RS\n3.puri-20RS')
#     choose=input('enter the dish:').lower()
#     quantity=int(input('enter the quantity:'))
#     if choose=='idli':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity*10}')
#     elif choose=='dosa':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity * 40}')
#     elif choose=='puri':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity * 20}')
#     else:
#         print('item not available..')
# elif option==2:
#     print('\t\tLUNCH MENU')
#     print(f'\t{'-' * 23}')
#     print('1.BIRYANI-220RS\n2.white_rice-110RS\n3.egg_rice-80RS')
#     choose = input('enter the dish:').lower()
#     quantity = int(input('enter the quantity:'))
#     if choose == 'biryani':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity *220 }')
#     elif choose == 'white_rice':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity * 110}')
#     elif choose == 'egg_rice':
#         print(f'---ORDER PALCED---\nAMOUNT TO BE PAID:{quantity * 80}')
#     else:
#         print('item not available..')

'''
wap to check login credential  of a customer
'''
# u_password={'dinga':1234,'dingi':4567}
# u_n=input('enter the user_name')
# if u_n in u_password:
#     password=int(input('enter the password'))
#     if password == u_password[u_n]:
#         print('login sucesfull.')
#     else:
#         print('invalid password..')
# else:
#     print('invalid user_name')

'''
wap to return 2nd heighest number among 3 numbers
'''
# a=int(input('enter the number:'))
# b=int(input('enter the number:'))
# c=int(input('enter the number:'))
#assume a is first heighest   then either b or c will be second heighest
# if a>b and a>c:
#     if b>c:
#         print(f'{b} is the second heighest')
#     else:
#         print(f'{c} is the second heighest')
# #assume b is first heighest   then either a or c will be second heighest
# elif b>a and b>c:
#     if a>c:
#         print(f'{a} is the second heighest')
#     else:
#         print(f'{c} is the second heighest')
# else:
#     if b>a:
#         print(f'{b} is the second heighest')
#     else:
#         print(f'{a} is the second heighest')



# dic={'vadapalani':1,'arumbakam':2,'cmbt':3,'anna_nagar':4,'tirumangalam':5}
# s_p=input('enter the start station:')
# e_p=input('enter the end stattion:')
# if s_p in dic and e_p in dic and s_p!=e_p:
#     no_of_stations=dic[e_p]-dic[s_p]
#     gender=input('enter m for male and f for female').lower()
#     if gender=='m':
#         option=input('enter a for adult and c for child ').lower()
#         if option=='a':
#             print('\t\t\tWELCOME TO MTC')
#             print(f'\t\t{'-'*15}')
#             print(f'\t\tstart:{s_p}\n\t\tend:{e_p}\n\t\tfare:{abs(no_of_stations*5)} RS')
#             print(f'\t\t{'-' * 15}')
#         elif option=='c':
#             print('\t\t\tWELCOME TO MTC')
#             print(f'\t\t{'-' * 15}')
#             fare=no_of_stations *5
#             print(f'\t\tstart:{s_p}\n\t\tend:{e_p}\n\t\tfare:{abs(fare-fare*15//100)} RS')
#             print(f'\t\t{'-' * 15}')
#         else:
#             print('invalid option..')
#     elif gender=='f':
#         print('\t\t\tWELCOME TO MTC')
#         print(f'\t\t{'-' * 15}')
#         fare = no_of_stations * 5
#         print(f'\t\tstart:{s_p}\n\t\tend:{e_p}\n\t\tfare:{0} RS')
#         print(f'\t\t{'-' * 15}')
#     else:
#         print('not valid..')
# else:
#     print('invalid station Name')









