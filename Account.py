from BankUtility import *

class Account:
    '''
    A class which represents an account

    ----------
    Attributes
    ----------
    First_Name : str
                first name of the accountholder
    Last_Name : str
                last name of the account holder
    account_Num : int
                The eight digit account number
    SSN : str
                the nine digit social security number of the account holder
    PIN : str
                four digit personal identification number
    Balance : 
                the balance in the account, in cents
    --------
    Methods
    --------
    set_Account_Num(AccountNum)
    get_Account_Num() 
    set_Owner_FName(FirstName)
    get_Owner_FName()
    set_Owner_LName(LastName) 
    get_Owner_LName()
    set_SSN(SSN)
    get_SSN() 
    set_PIN(PIN) 
    get_PIN() 
    set_Balance(Balance) 
    get_Balance() 
    deposit(amount)
    withdraw(amount) 
    isValidPIN(pin) 
        '''

    def __init__(self, FirstName = 'John', LastName ='Doe', AccountNum = 12345678, SSN = '123456789', PIN = '0000', Balance = 0.00):
        """constructs all attributes for account object"""
        self.__First_Name = FirstName
        self.__Last_Name = LastName
        self.__account_Num = AccountNum
        self.__SSN = SSN
        self.__PIN = PIN
        self.__Balance = Balance

    def __repr__(self):
        '''returns returns representation of account object'''
        return f'Account({self.__account_Num}, {self.__First_Name}, {self.__Last_Name}, {self.__SSN}, {self.__PIN}, {self.__Balance})'
    
    def __str__(self):
        '''returns string representation of the account object'''
        return f'''
        ============================================================
        Account number: {self.__account_Num}
        Owner First Name: {self.__First_Name}
        Owner Last Name: {self.__Last_Name}
        Owner SSN: {self.__SSN}
        PIN: {self.__PIN}
        Balance: ${self.__Balance}
        ============================================================
        '''
        
    
    def set_Account_Num(self, AccountNum):
        '''
        Sets AccountNum as integer
        ----------
        Parameters
        ----------
        AccountNum: int
                Number representing the 8 digit account number
        '''
        self.__account_Num = int(AccountNum)
       
    def get_Account_Num(self):
        '''returns account number '''
        return self.__account_Num

    def set_Owner_FName(self, FirstName):
        '''sets owner First name
        ----------
        Parameters
        ----------
        FirstName: str
                Fist name of the account holder
        '''
        self.__First_Name = FirstName

    def get_Owner_FName(self):
        '''returns first name of account owner'''
        return self.__First_Name
    
    def set_Owner_LName(self, LastName):
        '''
        Sets last name of account owner
        ----------
        Parameters
        ----------
        Lastname: str
                Last name of account holder
        '''
        self.__Last_Name = LastName

    def get_Owner_LName(self):
        '''returns last name of account owner'''
        return self.__Last_Name
    
    def set_SSN(self, SSN = '123456789'):
        '''setter method to change value of SSN
        ----------
        Parameters
        ----------
        SSN: str
                9 digit SSN of account holder
        '''
        SSN2 = SSN[5:9]

        self.__SSN = f'XXX-XX-{SSN2}'

    def get_SSN(self):
        '''returns social security number of account owner'''
        return self.__SSN
    
    def set_PIN(self, PIN = '0000'):
        '''setter method to change PIN value
        ----------
        Parameters
        ----------
        PIN: str
                4 digit PIN for account access
                '''
        self.__PIN = str(PIN)

    def get_PIN(self):
        '''returns PIN for account'''
        return self.__PIN
    
    def set_Balance(self, Balance = 0):
        '''sets balance from default of 0
        ----------
        Parameters
        ----------
        Balance: float
                Total Balance of account
        '''
        self.__Balance = float(Balance)
    
    def get_Balance(self):
        '''returns current balance of account'''
        return f'{self.__Balance}'  
    

    def deposit(self, amount = 'a'):
        '''
        prompts user to enter deposit amount, converts both deposit amount and current balance into cents,
        adds amount to balance, rounds to two decimal places, and converts back to dollars

        Returns string stating deposited amount
        ----------
        Parameters
        ----------
        amount:
                represents the amount  of money being deposited
        '''
        # To skip in testing etc
        while type(amount) == str:
            amount = (BankUtility.promptUserForPositiveNumber("Please enter the exact amount you would like to deposit:  "))    
        
        while amount > 0:
            #Checks amount is above 0, converts into cents for math
            print(f'Depositing ${amount}')
            amount = BankUtility.convertFromDollarsToCents(amount)
            Balance = BankUtility.convertFromDollarsToCents(self.__Balance)
            Balance =(Balance + amount) / 100
            self.__Balance =+ round(Balance, 2)
            #converts back into dollars and reports to user
            print(f"New Balance: ${self.__Balance}")
            return self.__Balance
        else:
            #Prints if entered amount is 0 or less
            print("You can only make deposits of amounts above zero")
            return False


    def withdraw(self, amount = 'a'):
        '''
        prompts user to enter withdrawal amount, converts both withdrawal and balance into cents
        makes sure the withdrawal amount is less than the balance
        if so; subtract, convert back to dollars and round to two decimal places

        If succesful, returns string stating amount withdrawn
        If not, returns string stating not enough and balance
        ----------
        Parameters
        ----------
        amount:
                represents the amount  of money being withdrawn from account
        '''
        # For purposes of skipping in testing
        while type(amount) == str:        
            amount = float(BankUtility.promptUserForPositiveNumber("Please enter the amount you would like to withdraw:  "))
        #Get amount and Balance saved to var
        Balance = self.__Balance
        #Makes sure the amount to be withdrawn is less than total balance
        if amount <= Balance:
            #prints amount withdrawn, convert the account's balance and amount to withdraw into cents
            print(f"Withdrawn: ${amount}")
            Balance = BankUtility.convertFromDollarsToCents(Balance)
            amount = BankUtility.convertFromDollarsToCents(amount)
             # Calculates new balance, converts back into dollars, and prints message to user
            Balance = (Balance - amount) /100
            self.__Balance = round(Balance, 2)
            print(f"New Balance: ${self.__Balance}\n")
            return self.__Balance
        else:
            #If amount is greater than balance, prints message
            print(f"Insufficient funds in account {self.__account_Num}! Your balance: ${self.__Balance}")
            return False

    
    def isValidPIN(self, pin = 0):
        '''
        prompts user for PIN. 
        If value entered is equal to stored value, returns True. 
        Else, returns false.
        ----------
        Parameters
        ----------
        pin:
                represents the PIN from user. checks whether equal to account object's stored PIN
        '''
        while type(pin) != str:
            pin = BankUtility.promptUserForString("What is your PIN?  ")

        if pin == self.__PIN:
            return True
        else:
            return False 
    
    
# a = Account() 
# # # b = Account()
# # # a.set_Account_Num()
# # # print(a.get_Account_Num())
# # # a.set_Owner_FName()
# # # print(a.get_Owner_FName())
# # # a.set_Owner_LName()
# # # print(a.get_Owner_LName())
# a.set_SSN('123456789')
# print(a.get_SSN())
# # # a.set_PIN()
# # # print(a.get_PIN())
# # # print(type(a.get_PIN()))
# # # print(a.isValidPIN())
# # print(a.get_Balance())
# # a.deposit()
# # print(a.get_Balance())
# # a.withdraw()
# # print(a.get_Balance())
# print(a)
