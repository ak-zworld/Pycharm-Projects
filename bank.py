user_password={'dinga':1234,'dingi':4567}
user_pin={'dinga':1111,'dingi':2222}
user_amt={'dinga':1000,'dingi':500}
def deposit(u_n):
    amt=int(input('enter the amount:'))
    pin=int(input('enter the pin:'))
    if pin==user_pin[u_n]:
        user_amt[u_n]=user_amt[u_n]+amt
        print(f'amount deposited sucesfully available balance is {user_amt[u_n]}')
    else:
        print('invalid pin')
def withdraw(u_n):
    amt = int(input('enter the amount:'))
    pin = int(input('enter the pin:'))
    if pin == user_pin[u_n]:
        if amt <=user_amt[u_n]:
            user_amt[u_n]=user_amt[u_n]-amt
            print(f'amount debited sucesfully available balance is {user_amt[u_n]}')
        else:
            print('insufficient balance')
    else:
        print('invalid pin..')
def balance_check(u_n):
    pin=int(input('enter the pin:'))
    if pin ==user_pin[u_n]:
        print(f'available balance is {user_amt[u_n]}')
    else:
        print('invalid pin..')
def signup():
    u_n=input('enter the user_name')
    password=int(input('enter the password'))
    pin=int(input('enter the pin'))
    amt=int(input('enter the amount to deposit'))
    if u_n not in user_password:
        user_password[u_n]=password
        user_pin[u_n]=pin
        user_amt[u_n]=amt
        print('account created sucesfully..')
    else:
        print('user name already exist..')
def login():
    u_n=input('enter the user_name')
    if u_n in user_password:
        password = int(input('enter the paswword'))
        if password==user_password[u_n]:
            print(f'1.deposit\n2.withdraw\n3.balance check')
            option=int(input('enter the option number:'))
            if option==1:
                deposit(u_n)
            elif option==2:
                withdraw(u_n)
            elif option==3:
                balance_check(u_n)
            else:
                print('invalid option..')
        else:
            print('invalid password')
    else:
        print('user_doesnot exist')
        signup()
print('\t\t\t\t\tWELCOME TO ABC BANK')
print(f'1.login\n2.signup')
choice=input('enter the option:').lower()
if choice=='login':
    login()
elif choice=='signup':
    signup()
else:
    print('invalid choice..')