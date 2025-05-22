''''''
'''
list comprehension

1.only for loop:--> [exp for variable_name in collection/range]
'''
#WAP TO CREATE A NEW LIST FROM THE EXISTING LIST
# lst=[1,2,3,4,5]
# res=[]
# for i in lst:
#     res.append(i)
# print(res)
#--------------------------------------------
#BY USING COMPREHENSION
# lst=[1,2,3,4,5]
# res=[i for i in lst]
# print(res)

# print([i for i in [1,2,3,4,5]])
#--------------------------------------------------------------
'''
2.BOTH FOR LOOP AND IF CONDITION

[exp for variable_name in collection/range if condition]
'''
#wap to create a new list with odd numbers present in the existing list
# lst=[1,2,3,4,5]
# res=[]
# for i in lst:
#     if i%2==1:
#         res.append(i)
# print(res)
#BY USING COMPREHENSION
# res=[i for i in lst if i%2==1]
# print(res)

'''
FOR LOOP ,IF AND ELSE
[exp if condition else exp for variable_nmae in collection/range]
'''
#wap to create a list from the existing list if the element is even do square and add
#else cube the element and add
# lst=[1,2,3,4,5,6,7,8,9,10]
# res=[]
# for i in lst:
#     if i % 2==0:
#         res.append(i**2)
#     else:
#         res.append(i**3)
# print(res)
#BY USING COMPREHENSION
#--------------------------------------------------
# res=[i**2 if i%2==0 else i**3 for i in lst]
# print(res)

#wap to create a new list if the element is ending with 0 add 100 else add 50
# lst=[1234,1000,1200,3457]
# res=[]
# for i in lst:
#     #i---1234
#     if i%10==0:
#         res.append(i+100)
#     else:
#         res.append(i+50)
# print(res)
#BY USING COMPREHENSION
# res=[i+100 if i%10==0 else i+50 for i in lst]
# print(res)

'''
wap to create a new list by raising the element to it's power
lst=[1,2,3,4,5,6,7]
o/p:--->> [1,2,9,64,...]
'''
# lst=[1,2,3,4,5,6,7]
# res=[]
# for i, j in enumerate(lst):
#     #i--->> index  j----ele
#     res.append(j**i)
# print(res)

# res=[lst[i]**i for i in range(len(lst))]
# print(res)
# res=[j**i for i,j in enumerate(lst)]
# print(res)

'''
wap to create a list if the element is having even length reverse the element and add
else add length of the element
'''
# lst=['dinga','orange','ramu','mangi']
# # o/p: [5,egnaro,umar,5]
# res=[i[::-1] if len(i)%2==0 else len(i) for i in lst]
# print(res)


'''
set comprehension
'''
#1.only for loop
'''
{exp for i in collection/range}
'''
#wap to create a set from a list by squaring the elements
# lst=[1,2,3,4,5,5,6,6,7,1]
# s=set()
# for i in lst:
#     s.add(i**2)
# print(s)
#BY USING COMPREHENSION

# res={i**2 for i in lst}
# print(res)

'''
2.BY USING BOTH FOR LOOP AND IF CONDITION
{exp for variable_name in collection/range if condition}
'''
#wap to create a set from the existing list if the elements are starting
# and ending with same letters
# lst=['amma','apple','malayalam','orange']
# s=set()
# for i in lst:
#     if i[0]==i[-1]:
#         s.add(i)
# print(s)

# res={i for i in lst if i[0]==i[-1]}
# print(res)

'''
3.FOR LOOP, IF and ELSE
{exp if condition else exp for i in collection/range}
'''
#wap to create a set from an existing set if the elements are starting
# with uppercase letter add as it is else reverse the element and add
# s={'Apple','Mango','orange','grapes'}
# res=set()
# for i in s:
#     if i[0].isupper():
#         res.add(i)
#     else:
#         res.add(i[::-1])
# print(res)

# res={i if i[0].isupper() else i[::-1] for i in s}
# print(res)


'''
DICTIONARY COMPREHENSION
1.ONLY FOR LOOP:
------------
{key:value for i in collection/range}
'''
# wap to create a dictionary from a list with key as index
# and value as element
# lst=[1,2,3,4,5,6]
# dic={}
# for i,j in enumerate(lst):
#     # i---index     j--element
#     dic[i]=j
# print(dic)

# dic={i:j for i,j in enumerate(lst)}
# print(dic)
'''
2.BOTH FOR LOOP AND IF CONDITION
{key:value for i in collection/range if condition}
'''
# wap to create a dictionary with key as first half of the
# element and value as second half if the length of the
# element is even
# lst=['facebook','instagram','twitter','whatsapp']
# dic={}
# for i in lst:
#     if len(i)%2==0:
#         key=i[:len(i)//2]
#         val=i[len(i)//2:]
#         dic[key]=val
# print(dic)

# d={i[:len(i)//2]:i[len(i)//2:] for i in lst if len(i)%2==0}
# print(d)
'''
FOR LOOP, IF,ELSE
{key:value if condition else value for variable_name in collection/range}
'''
# wap to create a dictionary with key as index and value
# as first half in reverse order if the element is ending with vowel
# else index and second half pair
# lst=['apple','facebook','instagram','orange']
# dic={}
# for i,j in enumerate(lst):
# #     i--- index    j--- element
#     if j[-1] in 'aeiouAEIOU':
#         val=j[:len(j)//2][::-1]
#         dic[i]=val
#     else:
#         dic[i]=j[len(j)//2:]
# print(dic)

# d={i:j[:len(j)//2][::-1] if j[-1] in 'aeiouAEIOU'
#     else j[len(j)//2:] for i,j in enumerate(lst)}
# print(d)

'''
wap to validate the password which was entered by the user from the 
front end
min 8 characters
1 upper
1 lower
1.number
1.special character
'''
import streamlit as st
name=st.text_input("NAME")
phno=st.number_input('PHNO',min_value=0)
email=st.text_input('EMAIL')
password=st.text_input('PASSWORD')
create=st.button('CREATE',type='primary')
if create:
    u_count = 0
    l_count = 0
    n_count = 0
    sp_count = 0
    if len(password) >= 8:
        for i in password:
            if i.isupper():
                u_count += 1
            elif i.islower():
                l_count += 1
            elif i.isdigit():
                n_count += 1
            else:
                sp_count += 1

        if u_count > 0 and l_count > 0 and sp_count > 0 and n_count > 0:
            st.success('password accepted..')
        else:
            st.error('password not accepted')

    else:
        st.warning('invalid length')





