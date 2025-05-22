# # ============ Characters ===================
# # . - Matches any character except new line
# # \. - Mathes a dot.
# # \* - Matches astrick
#
# # ============ Character set ===================
# # [abcd] - any character which matches either 'a' or 'b' or 'c' or 'd'
# # [^abcd] - any character but not 'a' or 'b' or 'c' or 'd'
# # [a-z] - any character between 'a' to 'z'
#
# # =========== Special Sequences ================
# # \w - Word character. Same as [a-zA-Z0-9_]. Matches alphanumeric and underscore.
# #\W - Non-Word Character. Same as [^a-zA-Z0-9_].
#                              Matches anything except alphanumeric and underscore .
# # \d - Matches a digit. Same as [0-9]
# # \D - Matches a Non-Digit. Same as [^0-9]
#
# # ========== Anchors ======================
# # ^ - Start of String
# # $ - End of String
#               function
#           ----------------
# findall:-->> it return's a list of values which are matched the pattern
#                else it returns empty list
import re
from sys import prefix

# import re
# s='hell\no eve\nry one'
# res=re.findall('.',s)
# print(res)
#['h', 'e', 'l', 'l', 'o', ' ', 'e', 'v', 'e', 'r', 'y', ' ', 'o', 'n', 'e']

# import re
# s='hello..every..'
# res=re.findall(r'\.',s)
# print(res)
#['.', '.', '.', '.']

# import re
# s='hell**o'
# res=re.findall(r'\*',s)
# print(res)
#['*', '*']
#-------------------------------------------------------------------------------------------
#wap to check whether given string is starting with vowel or not
# with out using in and not in
# import re
# s='bpple'
# res=re.findall('[aeiou]',s[0].lower())
# #res.findall('[aeiou]','a')  #Ture   --->> ['a']
# if res:
#     print('starting with vowel')
# else:
#     print('not starting with vowel')
#wap to check whether given string is ending with consonent or not
# with out using in and not in

# import re
# s='applq'
# res=re.findall('[^aeiou]',s[-1].lower())
# if res:
#     print('ending with consonent')
# else:
#     print('ending with vowel')


#wap to count no of alphabets present in a given string
# s='hello@123'
# import re
# res=re.findall('[a-z]',s)
# print(res)
#['h', 'e', 'l', 'l', 'o']

# s='HelLo@123'
# import re
# res=re.findall('[A-Z]',s)
# print(res)
#['H', 'L']
# s=input('enter the password:') #'HellO@123
# import re
# res=re.findall('[a-zA-Z]',s)
# print(f'{s} is having {len(res)} alphabets')


#wap to find no of digits present in a string
# s='hello@123'
# res=re.findall('[0-9]',s)
# print(f'{s} is having {len(res)} digits')
'''
wap to find no of special characters present in a string.
'''
# import re
# s='hello@#$123'
# res=re.findall('[a-zA-Z0-9]',s)
# print(res)
#['h', 'e', 'l', 'l', 'o', '1', '2', '3']

# import re
# s='hello@#$123'
# res=re.findall('[^a-zA-Z0-9]',s)
# print(f'{s} is having {len(res)} special characters')





#\w  :---------->>  [a-zA-Z0-9_]
# import re
# s='heLLo@_123'
# res=re.findall(r'\w',s)
# print(res)
#['h', 'e', 'L', 'L', 'o', '_', '1', '2', '3']

#\W :------>> [^a-zA-Z0-9_]
# import re
# s='heLLo@_123'
# res=re.findall(r'\W',s)
# print(res)
#['@']

#\d  :-----[0-9]
# import re
# s='hello@1234'
# res=re.findall(r'\d',s)
# print(res)
#['1', '2', '3', '4']

#\D ------[^0-9]
# import re
# s='hello@1234'
# res=re.findall(r'\D',s)
# print(res)
#['h', 'e', 'l', 'l', 'o', '@']

#^ :--- it is used to specify starting letter
# import re
# s='apple'
# res=re.findall('^a',s)
# print(res)
#['a']

#$ --- it is used to specify ending letter
# import re
# s='qspiders'
# res=re.findall('s$',s)   #[]
# if res:
#     print('given string is ending with s')
# else:
#     print('given string is not ending with s')

#starts with h end's with o
# import re
# s='hello'
# res=re.findall('^h.*o$',s)
# print(res)
#['hello']

#wap to check whether second letter of a string is "s" or not
# import re
# s='qspiders'
# res=re.findall('^.s..*',s)
# print(res)
#
# #['qspiders']






















