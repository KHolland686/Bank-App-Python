import random


class BankUtility:
    '''
    A class provides helper methods for the program
    --------
    Methods
    --------
    promptUserForString(prompt)
    promptUserForPositiveNumber(prompt)
    generateRandomInteger(min, max)
    convertFromDollarsToCents(amount)
    '''
    def promptUserForString(prompt):
        '''
        Helper function which saves and returns variable usr_str, taken from user input
        ----------
        Parameters
        ---------- 
        prompt: str
                Represents the prompt to be written when used. Asks for user input
        '''
        Usr_str = str(input(prompt))
        return Usr_str

    def promptUserForPositiveNumber(prompt):
        '''
        Helper function which gets and returns positive number from user input. Loops to check number correct type and positive
        ----------
        Parameters
        ---------- 
        prompt: str
                Represents the prompt to be written when used. Asks for user input
        '''
        posnum = 0
        while posnum <= 0:
            
            try:
                posnum = float(input(prompt))
                if posnum > 0:
                    return posnum
                else:
                    print('Number cannot be zero or negative. Try again.')
                    posnum = 0
            except ValueError:
                    print('Must be a number. Try again')
    
    def generateRandomInteger(min, max):
        '''
        Saves and returns random integer num from given a range
        ----------
        Parameters
        ---------- 
        min: int
                The minimum value in the range 
        max: int
                The maximum value in the range
        '''
        num = random.randint(min, max)
        return num
    
    def convertFromDollarsToCents(amount):        
        '''
        saves and returns variable 'cents; by multiplying given amount by 100 
        ----------
        Parameters
        ---------- 
        amount: float
                The dollar representation of the amount to be converted
        '''
        try:
            num=float(amount)
            cents = round(num, 2) * 100
            return int(cents)
        except ValueError:
            return False
    
    def isNumeric(numberToCheck):
        '''
        Checks if a given string is a number (long)
        This does NOT handle decimals.
      
        YOU DO NOT NEED TO CHANGE THIS METHOD
        THIS IS FREE FOR YOU TO USE AS NEEDED
      
        @param numberToCheck String to check
        @return true if the String is a number, false otherwise
        '''
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

# print(BankUtility.promptUserForPositiveNumber(2.75))
# print(BankUtility.convertFromDollarsToCents(42.4267567))