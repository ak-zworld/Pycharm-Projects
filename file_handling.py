# import os
# print('BEFORE CHANGING..')
# print(os.getcwd())
# os.chdir(r'C:\Users\QSP\Desktop')
# print('AFTER CHANGING..')
# print(os.getcwd())
#---------------------
# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# os.mkdir('e15')
'''
FileExistsError: [WinError 183] Cannot create a file
 when that file already exists: 'e15'
'''
#------------------------------------------------------------
# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# os.rmdir('e15')
#FileNotFoundError: [WinError 2]
# The system cannot find the file specified: 'e15'
#-------------------------------------------------------------
# import os
# os.chdir(r'C:\Users\QSP\Desktop')
# os.popen('w.txt','r')
#-------------------------------------------------------------
'''
variable_name = open('file_name','mode')
'''
# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# file=open('w.txt','r')
# # print(file.read())
# file.close()
# print(file.read()) #ValueError: I/O operation on closed file.
'''
with open('file_name','mode') as alias:
    stmt...
'''
# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('w.txt','r') as file:
#     # print(file.read())
#     pass
# print(file.read())   #ValueError: I/O operation on closed file.




# import os
# os.chdir(r'C:\Users\QSP\Desktop')
#WITH OUT USING CONTEXT
#--------------------------------------
# f=open('sample123.txt','r')
# # print(f.read())
# # print(f.readline()) #first line
# # print(f.readline())  #second line
# print(f.readlines())

#WITH USING CONTEXT MANAGER
# with open('sample.txt','r') as file:
    # print(file.read())
    # '''
    # brand	size	colour
    # adidas	10	white
    # puma	9	yellow
	#
    # nike	8	black
    # '''
    # print(file.readline()) #brand	size	colour
    # print(file.readline())  #adidas	10	white
    # print(file.readlines())
#['brand\tsize\tcolour\n', 'adidas\t10\twhite\n', 'puma\t9\tyellow\n', '\t\t\n', 'nike\t8\tblack\n']

# import os
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('sample.txt','r') as file:
#     header=next(file).split() #['brand',size ,colour]
#     print(header[0],header[-1])
#     for i in file:
#         if i.strip():
#             a=i.split()
#             if int(a[1])>8:
#                 print(a[0],a[-1])
#--------------------------
#WRITING INTO THE FILE
#-------------------------
#a--> mode
# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('s1.txt','a') as file:
#     file.write('hello\n')
#     file.writelines(
#         [
#             'good\n',
#             'bye\n',
#             'dinga\n'
#
#         ]
#     )



# import  os
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('sample.txt','r') as file:
#     with open('copy.txt','w') as fi:
#         for i in file:
#             fi.write(i)

# import os
# import csv
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('emp.csv','r') as file:
    # a=csv.reader(file)
    # print(list(a))
# '''
# [
# ['EMPLOYEE_ID', 'FIRST_NAME', 'LAST_NAME', 'EMAIL', 'PHONE_NUMBER',
# 'HIRE_DATE', 'JOB_ID', 'SALARY', 'COMMISSION_PCT', 'MANAGER_ID', 'DEPARTMENT_ID'],
#  ['198', 'Donald', 'OConnell', 'DOCONNEL', '650.507.9833', '21-JUN-07',
#  'SH_CLERK', '2600', ' - ', '124', '50']
#  ]
# '''
#     dic=csv.DictReader(file)
#     print(list(dic))
'''
[
{'EMPLOYEE_ID': '198', 'FIRST_NAME': 'Donald', 'LAST_NAME': 'OConnell',
 'EMAIL': 'DOCONNEL', 'PHONE_NUMBER': '650.507.9833', 'HIRE_DATE': '21-JUN-07', 
 'JOB_ID': 'SH_CLERK', 'SALARY': '2600', 'COMMISSION_PCT': ' - ', 'MANAGER_ID': '124',
  'DEPARTMENT_ID': '50'}, {'EMPLOYEE_ID': '199', 'FIRST_NAME': 'Douglas',
   'LAST_NAME': 'Grant', 'EMAIL': 'DGRANT', 'PHONE_NUMBER': '650.507.9844',
    'HIRE_DATE': '13-JAN-08', 'JOB_ID': 'SH_CLERK', 'SALARY': '2600', 'COMMISSION_PCT': ' - ',
     'MANAGER_ID': '124', 'DEPARTMENT_ID': '50'}
     ]
# '''
# import os
# import csv
# os.chdir(r'C:\Users\QSP\Desktop')
# with open ('new.csv','x'):
#     pass
#csv.writer()
# with open('new.csv','w',newline='') as file:
#     a=csv.writer(file)
#     # a.writerow(['dinga',1000,20])
#     a.writerows(
#         [
#             ['name','age','salary'],
#             ['dinga',20,1000],
#             ['dingi',20,2000,1234567890]
#
#         ]
#     )

# import os
# import csv
# os.chdir(r'C:\Users\QSP\Desktop')
# with open('new1.csv','w',newline='') as file:
#     f=csv.DictWriter(file,['name','age','salary'])
#     f.writeheader()
    # f.writerow(
    #     {'name':'manga','age':23,'salary':2003}
    # )
    # f.writerows(
    #     [
    #         {'name':'dinga','age':20,'salary':2000},
    #         {'name':'dingi','age':20,'salary':3000},
    #         {'name':'manga','age':21,'salary':4000}
    #     ]
    # )












#wap to find the factorial of a given number
# def fact(no):
#     if no==1:
#         return 1
#     else:
#         return no*fact(no-1)
#         '''
#         5*fact(4)
#         5*4*fact(3)
#         5*4*3*fact(2)
#         5*4*3*2*fact(1)
#         5*4*3*2*1====>> 120
#         '''
# print(fact(5))

#wap to find the sum of all the digits
#1234 ---->> 10
# def sum(no):
#     if no==0:
#         return 0
#     else:
#         return no%10+sum(no//10)
#     '''
#
#     '''
# print(sum(1234))
#

# def rev(s):
#     if s=='':
#         return ''
#     else:
#         return s[-1]+rev(s[:-1])
#         '''
#         o+rev(hell)
#         o+l+rev(hel)
#         o+l+l+rev(he)
#         o+l+l+e+rev(h)
#         o+l+l+e+h+rev('')
#         o+l+l+e+h+'' ===>> olleh
#         '''
# print(rev('hello'))



















