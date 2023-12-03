from Account import *
from BankUtility import *

class Bank:
    '''
    A class creating a bank object represented as an array
    --------
    Methods
    --------
    addAccountToBank(account):
    removeAccountFromBank(account):
    findAccount(accountNumber):
    ----------
    Attributes
    ----------
    Acc_Max :
            number representing the maximum length of the array of accounts
    Bank_array :
             List object representing the accounts in the bank
    
    '''
    def __init__(self, Acc_Max = 100):
        '''
        Constructor for Bank object
        initializes 'Bank_array' as a list of None, of length 'Acc_Max'
        '''
        self.Acc_Max = Acc_Max
        self.Bank_array = [None for i in range(self.Acc_Max)]     

    
    def addAccountToBank(self, account):
        '''
        Method to add an account object to the bank object

        Returns True if account added successfully
        Returns False if not (Max accounts in bank)
        -----------
        Parameters
        -----------
        account : 
                The account to be added to the Bank's array
        '''
        # iterates over the array, adds account if it finds a blank space ('None') and returns True
        for i in range(0, (self.Acc_Max)):
            if self.Bank_array[i] == None :
                self.Bank_array[i]= account
                return True
        else:
            #Prints message if account array is full
            print(f"There are already {self.Acc_Max} accounts registered!")
            return False; 


    def removeAccountFromBank(self, account):
        '''
        Method removing an account from the bank object

        Returns account obect(None) if found
        Returns False and prints message if not found
        -----------
        Parameters
        -----------
        account :
                The account object to be removed from the Bank's array
        '''
        #Iterates over array searching for account object
        for i in range(0, self.Acc_Max-1):
            if self.Bank_array[i] == account:
                self.Bank_array[i] = None
                return self.Bank_array[i]
            #If found it is removed and returned
        else:
            print(f'Account not found')
            return False
        #If not, message printed to user and returns False
        

    def findAccount(self, accountNumber = 0):
        '''
        Method which takes an account number and searches for the associated account in the bank array

        Returns the account if it exists
        else, returns None
        -----------
        Parameters
        -----------
        accountNumber:
                        The number used to search for an account with a matching number in the array
        '''
        for i in range(0, self.Acc_Max-1):
            if self.Bank_array[i] != None:
                account = self.Bank_array[i]
                if account.get_Account_Num() == accountNumber:
                    return account
        else:
            return None
        # for account in self.Bank_array:
        #     if account != None:
        #         if account.get_Account_Num() == accountNumber:
        #             return account

    def addMonthlyInterest(self, percent = 0):
        '''
        Method which takes annual interest from input
        from annual interest, calculates and adds interest monthly to all accounts in the array. 
        -----------
        Parameters
        -----------
        percent: float
                The annual interest rate taken from input

        '''
        l = []
        while percent == 0:
            percent = BankUtility.promptUserForPositiveNumber('Enter annual interest rate as percentage:  ')

        if percent > 0:
            monthly = (percent / 100) / 12

            for i in range(0,self.Acc_Max-1):
                if self.Bank_array[i] != None:  
                    account = self.Bank_array[i]
                    Bal = float(account.get_Balance())
                    month_Int = round(monthly * Bal, 2)
                    print(f'\nDeposited ${month_Int} monthly interest into account number: {account.get_Account_Num()}')
                    NewBal = Bal + month_Int
                    account.set_Balance(NewBal)
                    print(f'New Balance: ${account.get_Balance()}\n')
                    l.append(NewBal)
        return l
    



# a = Account(Balance=2500)
# b= Bank()
# c = Account(AccountNum= 123, Balance = 500)
# # a.set_Account_Num(12345678)
# # print(a.get_Account_Num())
# b.addAccountToBank(a)
# b.addAccountToBank(c)
# # # # # # print(b.Bank_array)
# # # # # # print(type(b.Bank_array[0]))
# # # # # # print(a)
# # print(b.findAccount(12345678))
# # print(b.findAccount(123))
# # # # print(a)
# # print(b.removeAccountFromBank(c))
# print(b.addMonthlyInterest(10))
