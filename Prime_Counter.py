import math #For using logarithm
import time #Exec time
import os #Clear console

def count_primes(limit,precise=False):
    '''
    A function that will execute all the
    calculating stuff for the program
    '''
    start_time = time.time()
    if not precise:
        '''
        Approximation for large numbers
        '''
        return(f'[{limit}]\n'
               f'------------------------------------------------------------------------\n'
               f'N° Primes ≅ {round(limit / math.log(limit))}\n' #limit/ln(limit) 
               f'Prime Density = {round((1/math.log(limit))*100, 2)}%' #1/ln(x)
               f'\n------------------------------------------------------------------------' 
               f"\n--- executed in {round(time.time() - start_time, 2)} seconds ---")
    else:
        '''
        Sieve of Eratosthenes
        '''
        print("Calculating...")
        list_to_limit = [True] * limit
        list_to_limit[0] = list_to_limit[1] = False
        for _ in range(2, int(limit ** 1 / 2) + 1):
            if list_to_limit[_]:
                for i in range(_ * _, limit, _):
                    list_to_limit[i] = False
        primes = [_ for _ in range(limit) if list_to_limit[_]]
        primes_lenth = len(primes)
        return (f'...\n\n[{limit}]\n'
                f'\nPrimes = {primes}\n\n'
                f'------------------------------------------------------------------------\n'
                f'N° Primes = {primes_lenth}\n'
                f'Prime Density = {round(limit/primes_lenth, 2)}%\n'
                f'-----------------------------------------------------------------------'
                f"\n--- executed in {round(time.time() - start_time, 2)} seconds ---")

def main():
    '''
    The main function for a user-friendly interface.
    '''
    print('             || Prime numbers ||                      ')
    print('|||| Know how many prime numbers exist till a limit ||||\n')
    while True:
        ask = int(input('Please enter a limit: '))
        if ask<1000:
            os.system('cls')
            print(count_primes(ask,True))
            break
        else:
            while True:
                print('\nWARNING! - For larger numbers, "precise" will take a long time!\n')
                print('˅˅˅')
                ask_two = int(input('Do you want it to be precise(1) or not(0)? --> '))
                if ask_two==1:
                    ask_two = True
                    os.system('cls')
                    print(count_primes(ask, ask_two))
                    break
                elif ask_two==0:
                    ask_two = False
                    os.system('cls')
                    print(count_primes(ask, ask_two))
                    break
                else:
                    os.system('cls')
                    print('ERROR: Please enter a valid number!')
                    continue
            break

while True:
    '''
    Check if the user wants to try again
    '''
    try:
        os.system('cls')
        main()
        ask_three = int(input('\nEnter (1) to try again or any character to exit -->'))
        if ask_three==1:
            continue
        else:
            break
    except:
        continue
os.system('cls')
exit()