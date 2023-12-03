

class CoinCollector:
    '''
    A class which acts as a coin machine and counts change.
    --------
    Methods
    --------
    parseChange(coins) :
                        Given a string of characters representing possible coins
                        calculates and returns the total amount it represents in dollars and cents.
    '''
    def parseChange(coins):
        '''
        Calculates the total amount of money, in cents, from a given string
        ----------
        Parameters
        ----------
        coins : str
                A string containing letter representation of the coins to be counted

            P = Pennies
            N = Nickels
            D = Dimes
            Q = Quarters
            H = Half-dollar
            W = Whole dollar

            If a letter outside of these is used, it will be printed as unrecognizable and ignored.
        -------
        Returns
        -------
        total : 
                representing the total amount counted as cents
        '''
        total = 0
        for coin in coins:
            if coin.upper() =='P':
                total += 1
            elif coin.upper() == 'N':
                total += 5
            elif coin.upper() == 'D':
                total += 10
            elif coin.upper() == 'Q':
                total += 25
            elif coin.upper() == 'H':
                total += 50
            elif coin.upper() == 'W':
                total += 100
            else:
                print(f'Incorrect coin found {coin}. Not counted')
                total += 0
        return int(total)
    

# print(CoinCollector.parseChange('PPPNDQQHHWWZ'))
