''''''
# for i in range(5):
#     for j in range(5):
#         print('*',end=' ')
#     print()
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''
# for i in range(5):
#     for j in range(5):
#         print((i,j),end=' ')
#     print()
'''
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i==0 or j==0 or i==no-1 or j==no-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i==no//2 or j==no//2 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
    *     
    *     
* * * * * 
    *     
    *    
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i==j :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*         
  *       
    *     
      *   
        * 

'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i+j==no-1 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
        * 
      *   
    *     
  *       
*     
'''
# no=11
# for i in range(no):
#     for j in range(no):
#         if (i==0 or j==0 or i==no-1 or j==no-1 or i==no//2 or j==no//2 or
#                 i==j or i+j==no-1 ):
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * * * * * * * 
* *       *       * * 
*   *     *     *   * 
*     *   *   *     * 
*       * * *       * 
* * * * * * * * * * * 
*       * * *       * 
*     *   *   *     * 
*   *     *     *   * 
* *       *       * * 
* * * * * * * * * * * 

'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if j==0 or i==no-1 or i==j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*         
* *       
*   *     
*     *   
* * * * * 
'''




# no=5
# for i in range(no):
#     for j in range(no):
#         if j==0 or i==0 or i+j==no-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
*     *   
*   *     
* *       
*    
'''

# no=5
# for i in range(no):
#     for j in range(no):
#         if i==no-1 or j==no-1 or i+j==no-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
        * 
      * * 
    *   * 
  *     * 
* * * * *
'''

# no=5
# for i in range(no):
#     for j in range(no):
#         if i==0 or i==j or j==no-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
* * * * * 
  *     * 
    *   * 
      * * 
        * 
'''
# no=11
# for i in range(no):
#     for j in range(no):
#         if j==0 or i==j or j==no-1 or i+j==no-1:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*                   * 
* *               * * 
*   *           *   * 
*     *       *     * 
*       *   *       * 
*         *         * 
*       *   *       * 
*     *       *     * 
*   *           *   * 
* *               * * 
*                   * 
'''

# no=5
# for i in range(no):
#     for j in range(no):
#         if j==0 or j==no-1 or i==j and i<=no//2 or i+j==no-1 and i<=no//2:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*       * 
* *   * * 
*   *   * 
*       * 
*       *
'''

# no=5
# for i in range(no):
#     for j in range(no):
#         if j==0 or j==no-1 or i==j and i>=no//2  or i+j==no-1 and i>=no//2 :
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*       * 
*       * 
*   *   * 
* *   * * 
*       * 
'''






'''
(0, 0) 
(1, 0) (1, 1) 
(2, 0) (2, 1) (2, 2) 
(3, 0) (3, 1) (3, 2) (3, 3)
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i>=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
*         
* *       
* * *     
* * * *   
* * * * * 
'''

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
# no=5
# for i in range(1,no+1):
#     for j in range(1,no+1):
#         if i>=j:
#             print(j,end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# no=5
# for i in range(no):
#     for j in range(no):
#         if i>=j:
#             print(j+1,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# no=5
# for i in range(1,no+1):
#     for j in range(1,no+1):
#         if i>=j:
#             print(i,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
# no=5
# for i in range(no):
#     for j in range(no):
#         if i>=j:
#             print(i+1,end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
1         
2 2       
3 3 3     
4 4 4 4   
5 5 5 5 5 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i>=j:
#             print(chr(97+j),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
a         
a b       
a b c     
a b c d   
a b c d e 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i>=j:
#             print(chr(97+i),end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
a         
b b       
c c c     
d d d d   
e e e e e 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i==0 and j!=0 and j!=no-1 or j==0 and i!=0 or i==no//2 or j==no-1 and i!=0:
            #      *** or ***
#          if i==0 and 0<j<no-1 or j==0 and i!=0 or i==no//2 or j==no-1 and i!=0:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
  * * *   
*       * 
* * * * * 
*       * 
*       * 
'''
# no=5
# for i in range(no):
#     for j in range(no):
#         if i==0 and j!=0 or j==0 and 0<i<no-1 or i==no-1 and j!=0:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()
'''
  * * * * 
*         
*         
*         
  * * * * 
'''

# no=5
# for i in range(1,no+1):
#     print('*'*i,end='')
#     print(' '*(no-i)*2,end='')
#     print('*'*i,end='')
#     print()
'''
*        *
**      **
***    ***
****  ****
**********
'''

# no=5
# for j in range(5,0,-1):
#     print('*'*j,end='')
#     print(' '*(no-j)*2,end='')
#     print('*'*j,end='')
#     print()
'''
**********
****  ****
***    ***
**      **
*        *
'''
# no=5
# for i in range(1,no+1):
#     print('*'*i,end='')
#     print(' '*(no-i)*2,end='')
#     print('*'*i,end='')
#     print()
# for j in range(5,0,-1):
#     print('*'*j,end='')
#     print(' '*(no-j)*2,end='')
#     print('*'*j,end='')
#     print()

'''
*        *
**      **
***    ***
****  ****
**********
**********
****  ****
***    ***
**      **
*        *
'''

# no=5
# for i in range(1,no+1):
#     print(' '*(no-i),end='')
#     print('* '*i,end='')
#     print()
'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
'''
# no=5
# for j in range(no,0,-1):
#     print(' '*(no-j),end='')
#     print('* '*j,end='')
#     print()
'''
* * * * * 
 * * * * 
  * * * 
   * * 
    *
'''
# no=5
# for i in range(1,no+1):
#     print(' '*(no-i),end='')
#     print('* '*i,end='')
#     print()
# for j in range(no-1,0,-1):
#     print(' '*(no-j),end='')
#     print('* '*j,end='')
#     print()

'''
    * 
   * * 
  * * * 
 * * * * 
* * * * * 
 * * * * 
  * * * 
   * * 
    * 
'''


# no=5
# for j in range(no,0,-1):
#     print(' '*(no-j),end='')
#     print('* '*j,end='')
#     print()
# for i in range(1,no+1):
#     print(' '*(no-i),end='')
#     print('* '*i,end='')
#     print()
'''
 * * * * *  
  * * * *  
   * * *  
    * *  
     *  
     *  
    * *  
   * * *  
  * * * *  
 * * * * * 
'''



















