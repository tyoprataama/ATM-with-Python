'''
Hi, I'm Tyo. College student from Economic background but really love computer science, because since I can run 'Hello World',
I can feel the power of my hand!!
Enjoy your code!
'''
from distutils.log import error
import random
import datetime
from costumer import Costumer

atm = Costumer(id)

#Loop PIN
while True:
    id = int(input('\n Enter your PIN : '))
    count = 0
    #IF PIN False
    while (id != int(atm.prev_pin) and count < 3 ):
        id = int(input('Wrong PIN, Enter your PIN again : '))
        count += 1
        
        if count == 3:
            print('Error, pick up your card from the machine : ')
            exit()
    #IF PIN True        
    while True:
        print('\n                                  Welcome to Python Bank')
        print('\n 1 - Check Balance \t 2 - Debit \t 3 - Deposit \t 4 - Change PIN \t 5 - Log Out')
        select = int(input('\n Choose the menu : '))
        #Choose the menu
        if select == 1:
            print('\n Your balance is $ ' + str(atm.check_saldo()) + '\n')
            
        elif select == 2:
            nominal = float(input('\n Enter the Debit Value : $ '))
            verify = input('\n You really want to take $ ' + str(nominal) + ' from your bank account ? ( y / n ) : ' + ' ')
            if verify == 'y':
                print('\n Your currently balance is $ ' + str(atm.check_saldo()) + ' ')
            else:
                break
            if nominal < atm.check_saldo():
                atm.debit_c(nominal)
                print('\n Your transactions succesfully')
                print('\n Your current balance is $ ' + str(atm.check_saldo()) + ' ')
            else:
                print('\n Transactions failed, your account is out of balance')
                print('\n Please add your balance before doing this transactions!')
                
        elif select == 3:
            nominal = float(input('\n Enter the Deposit Value : $ '))
            verify_d = input('\n You really want to save $ ' + str(nominal) + ' to your bank account ? ( y / n ) : ' + ' ')
            if verify_d == 'y':
              atm.deposit_c(nominal)
              print('\n Your current balance is $ ' + str(atm.check_saldo()) + '\n')
            else:
                break
           
        elif select == 4:
            verify_p = int(input('\n Enter your PIN : '))
            
            while verify_p != int(atm.check_pin()):
                wrong_p = int(input('Wrong PIN! Try again : '))
                if wrong_p == int(atm.check_pin()):
                    print('\n Log in successfully')
            if verify_p == int(atm.check_pin()):
                    print('\n Log in successfully')
                    
                    while True:
                        new_pin = int(input('\n Enter your new PIN : '))
                        v_pin = int(input('\n Verify your PIN : '))
            
                        if new_pin == v_pin:
                            print('\n Your PIN successfully updated! \n')
                            break
                        
                        elif new_pin != v_pin:
                            print('Wrong PIN! Try again : ')
                        

                
        elif select == 5:
            print('')
            print('         Python Bank         ')
            print(' ')
            print('Number Reff : ', random.randint(100000, 1000000))
            print('Date        : ', datetime.datetime.now())
            print('Balance     : $ ', atm.check_saldo())
            print(' ')
            print(' Thank you to used Python Bank!  ')
            print('')
            exit()
        else:
            print('Error. Sorry unexpected number!')
            