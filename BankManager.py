from BankUtility import *
from Account import *
from Bank import *
from CoinCollector import *

class BankManager:
    '''
    Class which instantiates a Bank object when run
    ----------
    Attributes
    ----------
    bank1:
            The instantiated Bank object which will be used for the accounts
    -------
    Methods
    -------
    promptForAccountNumberandPIN(bank):
                Acts as a log-in function, asks for account number and PIN and returns the matching account
    main():
                Sets up the transaction screen, and provides all functionality for each transaction
    '''
    def __init__(self, ):
        '''
        Constructor for BankManager program. 
        Initializes a Bank object
        '''
        self.bank1 = Bank()
       
    @staticmethod    
    def promptForAccountNumberAndPIN(bank):
        '''
        Main log-in function. Prompts user to enter their account number and searches the Bank object for that account
        If the account is found, prompts user to enter their PIN.

        Returns the account accessed if account number and PIN match
        Returns None and prints message otherwise
        -----------
        Parameters
        -----------
        bank: obj
            represents the bank holding the accounts
        '''
        acc = int(BankUtility.promptUserForString("Please enter your Account Number:  "))
        # get input for account number and search for corresponding account
        Usr_account = bank.findAccount(acc)
        if Usr_account == None:
            #If not found, print message and return None
            print(f"Account not found for account number: {acc}")
            return None

        else:
            # If account is found, get input for PIN number and check if it matches
            # Loop until Valid PIN entered
            # print(bank.Bank_array)
            key = BankUtility.promptUserForString("Account found. Enter your PIN:  ")
            if Usr_account.isValidPIN(key):
                return Usr_account
            else:
                print(f'Invalid PIN!')
        

        
    def main(self):
        '''
        Main transaction menu. sets up each transaction for choices 1 - 11. 
        User enters the menu number corresponding to the transaction they wish to perform.
        Each transaction will run and then return to main menu.
        
        '''
        choice = 0
        while choice == 0:
            #initialize choice to zero and have main menu display
            print('''
            ============================================================
            What do you want to do?
            1. Open an account
            2. Get account information and balance
            3. Change PIN
            4. Deposit money in account
            5. Transfer money between accounts
            6. Withdraw money from account
            7. ATM withdrawal
            8. Deposit change
            9. Close an account
            10. Add monthly interest to all accounts
            11. End Program
            ============================================================
            ''')
            # print(self.bank1.Bank_array)
            #Get input from user for which number transaction they wish to perform
            choice = BankUtility.promptUserForPositiveNumber(
                "Please enter the number corresponding to the transaction you would like to perform:  ")
            if 0 > choice or choice > 11:
                # In case of invalid number
                print("Invalid choice. Please try again")
                choice = 0


            elif choice == 1: #OPEN ACCOUNT
                #Create new account, prompt user for First and Last Names
                NewAcc = Account()
                FName = BankUtility.promptUserForString("What is your first name?  ")
                NewAcc.set_Owner_FName(FirstName = FName)
                LName = BankUtility.promptUserForString("What is your last name?  ")
                NewAcc.set_Owner_LName(LastName = LName)
                #Set SSN from user input, checking that it is 9 digits long and consists of numbers
                ssn = 'a'
                while len(ssn) != 9:
                    ssn = BankUtility.promptUserForString("Please enter your Social Security Number (9 digits):  ")
                    if ssn.isnumeric():
                        if len(ssn) == 9:
                            NewAcc.set_SSN(ssn)
                        else:
                            print(f'SSN must be 9 digits!')
                    else:
                        print('Your SSN must be numbers only!')
                        ssn = 'a'
                #generate random 4 digit number for PIN
                pin = str(BankUtility.generateRandomInteger(0, 9999))
                NewAcc.set_PIN(PIN = pin)
                # Generate random account number as 'num'. Check if account already exists with that number
                # if so, try different 8 digit number until finds new one
                num = BankUtility.generateRandomInteger(10**7, 99999999)
                while self.bank1.findAccount(num) != None:
                    num = BankUtility.generateRandomInteger(10**7, 99999999)
                else:
                    NewAcc.set_Account_Num(num)
                #Finally, add the accouunt to the bank object
                self.bank1.addAccountToBank(NewAcc)
                print(NewAcc)
                #reset choice to 0 at the end of each transaction
                choice = 0


            elif choice == 2: #GET ACCOUNT INFO
                #Search for existing account from given account number and PIN
                info = None
                count = 0
                #Gives user a certain number of tries to enter correct info before reverting to main menu
                while count < 5:
                    info = BankManager().promptForAccountNumberAndPIN(self.bank1)
                    count +=1
                    if info != None:
                        print(info) 
                        count = 6
                        choice = 0
                    else:
                        print(f"Invalid! Try again, you have used {count} out of 5 attempts . . .")
                        choice = 0
                    if count == 5:
                        print('Max attempts reached! Exiting . . .')
                        choice = 0


            elif choice == 3: #CHANGE PIN
                #Gathers account info from given account number and PIN
                acc = BankManager().promptForAccountNumberAndPIN(self.bank1)
                # print(acc)
                new_PIN2 = 0
                #Prompts user to enter new PIN, makes sure it is both 4 digits and numeric
                while new_PIN2 == 0:
                    new_PIN = BankUtility.promptUserForString('Enter New PIN:  ')
                    if len(new_PIN) == 4:
                        if new_PIN.isnumeric():
                            #If both conditions pass, asks user to input new PIN again
                            new_PIN2 = BankUtility.promptUserForString('Enter New PIN again to confirm:  ')
                            #Makes sure both entries match and updates
                            if new_PIN == new_PIN2:
                                acc.set_PIN(PIN = new_PIN)
                                print(f'PIN updated.')
                                choice = 0
                            else:
                                print('Numbers entered do not match. Try again.')
                                new_PIN2 = 0
                        else:
                            print(f'{new_PIN} is not a number. Try again.')
                    else:
                        print(f"PIN '{new_PIN}' must be four digits")


            elif choice == 4: #DEPOSIT MONEY
                depacc = BankManager().promptForAccountNumberAndPIN(self.bank1)
                #Takes input for account number and PIN and checks for it's existence
                if depacc != None:
                    #If account exists, runs deposit function to get deposit amount and add to balance
                    depacc.deposit()
                    choice = 0
                else:
                     print("Invalid! Returning to main screen . . .")
                     choice = 0


            elif choice == 5: #TRANSFER MONEY
                #Checks for existence of account to transfer from first
                print('\nAccount to Transfer From:')
                transfFrom = BankManager().promptForAccountNumberAndPIN(self.bank1)
                if transfFrom != None:
                    #Then checks for existence of account to transfer to
                    print('\nAccount to Transfer To:')
                    transfTo = BankManager().promptForAccountNumberAndPIN(self.bank1)
                    if transfTo != None:
                        #asks user to input amount to transfer
                        transfAmount = BankUtility.promptUserForPositiveNumber('Enter amount to transfer:$  ')
                        #Withdraws amount from first acc, deposits in second
                        transfFrom.withdraw(transfAmount)
                        transfTo.deposit(transfAmount)
                        #Print balance of both
                        print(f'\nAccount {transfFrom.get_Account_Num()} New Balance: ${transfFrom.get_Balance()}')
                        print(f'Account {transfTo.get_Account_Num()} New Balance: ${transfTo.get_Balance()}')
                        choice = 0
                else:
                    print("Invalid! Returning to main screen . . .")
                    choice = 0


            elif choice == 6:#WITHDRAW MONEY
                # Sets account for withdrawal based on input for account number and PIN
                withdacc = BankManager().promptForAccountNumberAndPIN(self.bank1)
                if withdacc != None:
                    #If it finds account, runs withdrawal function
                    withdacc.withdraw()
                    choice = 0
                else:
                    # if not, back to beginning
                    print("Invalid! Returning to main screen . . .")
                    choice = 0
            

            elif choice == 7: #ATM WITHDRAWAL
                #sets account based on input for account number and PIN
                atm = BankManager().promptForAccountNumberAndPIN(self.bank1)
                if atm != None:
                    atm_amount = 1
                    #If there is a matching account, asks for amount
                    while atm_amount == 1:
                        atm_amount = BankUtility.promptUserForPositiveNumber('Enter amount to withdraw in multiples of $5 up to $1000 (no cents):  ')
                        if atm_amount % 5 != 0:
                            #If the amount isn't a multiple of 5, lets user know and starts again
                            print(f'You can only withdraw in multiples of $5!! You entered {atm_amount}')
                            atm_amount = 1

                        else:
                            # uses floor division and calculates number of each denomination of bill to be distributed
                            #prints total amount and number of each type of bill
                            remainder = int(atm_amount)
                            atm.withdraw(amount = atm_amount)
                            twenties = remainder // 20
                            print(f'Number of twenty dollar bills: {twenties}')
                            remainder -= (twenties * 20)

                            tens = remainder // 10
                            print(f'Number of ten dollar bills:  {tens}')
                            remainder -= (tens * 10)

                            fives = remainder // 5
                            print(f'Number of five dollar bills:  {fives}')                           
                            choice = 0
                else:
                    print("Invalid! Returning to main screen . . .")
                    choice = 0 
                        

            elif choice == 8:#DEPOSIT CHANGE
                #Gets user input to find account
                coin_acc = BankManager().promptForAccountNumberAndPIN(self.bank1)
                if coin_acc != None:
                    #If account exists, ask what coins to be deposited
                    coin_depo = BankUtility.promptUserForString('P = 1 penny, N = 1 nickel, D = 1 dime, Q = 1 quarter, H = 1 half-dollar, W = 1 whole dollar\nDeposit coins:  ')
                    parsed = CoinCollector.parseChange(coin_depo)
                    # Parses change and states amount in dollars
                    depoInDollars = (parsed / 100)
                    print(f'${depoInDollars} in coins deposited in account')
                    #Runs deposit function
                    coin_acc.deposit(depoInDollars)
                    choice = 0
                else:
                    print("Invalid! Returning to main screen . . .")
                    choice = 0 


            elif choice == 9:#CLOSE ACCOUNT
                # Finds account to be closed from user input
                close_acc = BankManager().promptForAccountNumberAndPIN(self.bank1)
                if close_acc != None:
                    #If account found, removes it from bank and prints message to user
                    self.bank1.removeAccountFromBank(close_acc)
                    print(f'Account {close_acc.get_Account_Num()}  Closed.')
                    # print(self.bank1.Bank_array)
                    choice = 0
                else:
                    print("Invalid! Returning to main screen . . .")
                    choice = 0 


            elif choice == 10: #ADD MONTHLY INTEREST TO ALL ACCOUNTS
                self.bank1.addMonthlyInterest()
                choice = 0
                    
            elif choice == 11: #TO QUIT
                print('\nThanks for banking with us today!\n')
                break


# instanstialize BankManager obj and run main function

BankMgr = BankManager()

BankMgr.main()
# print(BankManager().bank1.Bank_array)

