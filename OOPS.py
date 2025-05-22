# class Bank:
#     #GENERAL STATES
#     b_name='icici'
#     ifsc_code='ici012345'
#     address='vadapalani'
#     def __init__(self,cname,phno,ac_no):
#         # SPECIFIC STATES
#         self.customer_name=cname
#         self.phno=phno
#         self.ac_no=ac_no
#     def details(self):
#         print(f'BANK_NAME:{self.b_name}\nIFSC_CODE:{self.ifsc_code}\n'
#               f'BANK_ADDRESS:{self.address}\nCUSTOMER_NAME:{self.customer_name}\n'
#               f'CUSTOMER_PHNO:{self.phno}\nCUSTOMER_ACCOUNT_NO:{self.ac_no}')
# dinga=Bank('dinga',1234567891,11122200)
# dingi=Bank('dingi',1234567892,111122233)
# dinga.details()
# print('='*40)
# dingi.details()  #Ox13




# class Father:
#     def land(self):
#         print('50 acres of land')
# class Son(Father):
#     def house(self):
#         print('3BHK')
# s=Son()
# s.house()
# s.land()
#
# class whatsapp_v1:
#     def chat(self):
#         print('10000 lines ')
#     def vdocall(self):
#         print('5000 lines')


# class GrandFather:   #SUPER CLASS
#     def gold(self):
#         print('3kg of gold')
# class Father(GrandFather):  #SUBCLASS
#     #gold
#     def land(self):
#         print('50 acres of land')
# class Son(Father):   #SUBCLASS
#     #gold
#     #land
#     def house(self):
#         print('3BHK')
# f=Father()
# f.land()
# f.gold()
# #====================================
# s=Son()
# s.house()
# s.gold()
# s.land()


# class Father:  #SUPER CLASS
#     def land(self):
#         print('50 acres of land')
# class Mother:  #SUPER CLASS
#     def gold(self):
#         print('3kg of gold')
# class sample:
#     pass
# class Son(Father,Mother):
#     def house(self):
#         print('3BHK')
# s=Son()
# s.gold()
# s.land()
# s.house()

# class Father:   #SUPER CLASS
#     def land(self):
#         print('50 acres of land')
# class Son1(Father):
#     def house(self):
#         print('3BHK ')
# class Son2(Father):
#     def car(self):
#         print('BMW')
# s=Son1()
# s.house()
# s.land()
# print('='*50)
# s1=Son2()
# s1.land()
# s1.car()

# class Animal:
#     def sound(self):
#         print('animal sound')
# class Lion(Animal):
#     #sound
#     def hunting(self):
#         print('hunting..')
# class Tiger(Animal):
#     #sound
#     def running(self):
#         print('running')
# class Liger(Lion,Tiger):
#     #sound hunting running
#     def height(self):
#         print('height')
# l=Liger()
# l.sound()
# l.height()
# l.hunting()
# l.running()

''''''
'''
method overriding
'''
# class whatsapp:
#     def chat(self):
#         print('loc gifs contact')
# class whatsapp_v2(whatsapp):
#     def chat(self):
#         super().chat()
#         print('payment')
#
# w=whatsapp_v2()
# w.chat()
'''
polymorphisam
'''
#wrt len() function
#-------------------------
#string
# s='hello'
# print(len(s)) # no. of characters
# #list
# lst=['hello','hi','good']
# print(len(lst)) # no. of elements
# #dictionary
# dic={'a':1,'b':2,'c':3}
# print(len(dic))  # no.of keys

#2.w.r.t operators
#--------------------------------
'''
+
'''
#integer
# print(10+20)  #addition
# #string
# print('hello'+'hi')  #concatination
#
# #list
# print([1,2,3]+[4,5,6])  #merging
'''
*
'''
#integer
# print(2*3)  #multiplication
# #string
# print('hi'*3) #replication
# print([1,2]*4) #replication
'''
-
'''
#integer
# print(3-1) # subtraction
# #set
# print({1,2,3}-{3,4,5})  #difference
# print({1,2,3}.difference({3,4,5}))


#WRT CLASS AND METHOD
#-------------------------
# class Manager:
#     def credit_bill(self):
#         print('phone_bill,electricity')
# class Employee(Manager):
#     def credit_bill(self):
#         print('betting,laptop')
# m=Manager()
# e=Employee()
# m.credit_bill()
# e.credit_bill()


#WRT inheritance
# -----------------

# class vehical:
#     def __init__(self,name,speed):
#         self.brand=name
#         self.speed=speed
#     def type(self):
#         print('type of vehicals')
# class car(vehical):
#     def type(self):
#         print('MOVE!')
# class Boat(vehical):
#     def type(self):
#         print('SAIL!')
# class Flight(vehical):
#     def type(self):
#         print('FLY!')
# def mediator(obj):   #ox11
#     print(obj.brand)   #ox11.brand | |   #ox12.brand
#     print(obj.speed)   #ox11.speed ||   #ox12.speed
#     obj.type()         #ox11.type     ||  #ox12.type()
# c=car('BMW',220)
# b=Boat('Reel Ambition',20)
# f=Flight('Boeing',250)
# mediator(c)  #0x11 --->>> mediator(ox11)
# print('='*30)
# mediator(b)   #ox12--->> mediator(ox12)
# print('='*30)
# mediator(f)
'''
BMW
220
MOVE!
==============================
Reel Ambition
20
SAIL!
==============================
Boeing
250
FLY!
'''







# class instagram:
#     def story(self):
#         print('5000 lines...')
#     def reels(self):
#         print('5000 lines..')
#     def post(self):
#         print('2000 lines')
#
# i=instagram()
# i.reels()
# i.story()
# i.post()

# from abc import ABC,abstractmethod
# class sample(ABC):   #ABSTRACT CLASS
#     @abstractmethod
#     def story(self):
#         pass
#     @abstractmethod
#     def post(self):
#         pass
#     @abstractmethod
#     def reels(self):
#         pass
#     @abstractmethod
#     def chat(self):
#         pass
#     @abstractmethod
#     def vdocall(self):
#         pass
#     def gifs(self):   #CONCRETE METHOD
#         print('gifs')
# class instagram(sample):
#     def story(self):
#         print('story')
#     def vdocall(self):
#         print('vdocall')
#     def chat(self):
#         print('chatting')
#     def reels(self):
#         print('reels')
#     def post(self):
#         print('post')
# i=instagram()
# i.chat()
# i.reels()
# i.post()
# i.story()
# i.vdocall()
# i.gifs()



# class bank:
#     def __init__(self,name,balance):
#         self.name=name
#         self.__balance=balance
#     def get_balance(self):
#         u_name=input('enter the user_name').lower()
#         pin=int(input('enter the pin:'))
#         if u_name=='dinga':
#             if pin ==1234:
#                 print(self.__balance)
#             else:
#                 print('invalid pin')
#         else:
#             print('invalid user_name')
#     def set_balance(self):
#         u_name = input('enter the user_name').lower()
#         pin = int(input('enter the pin:'))
#         if u_name == 'dinga':
#             if pin == 1234:
#                 amt=int(input('enter the amount:'))
#                 self.__balance+=amt

# dinga=bank('dinga',1000)
# dingi=bank('dingi',500)
# # dinga.get_balance()
# # dingi.get_balance()
# dinga.get_balance()
# print('for deposit')
# dinga.set_balance()
# print('after deposit')
# dinga.get_balance()










