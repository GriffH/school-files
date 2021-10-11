from random import randint


def guessing_game():
    n = randint(1,100)  # get random
    # print(n) remove # for easy mode
    while True:
        while True:
            try:
                guess = int(input('Guess an integer between 1 and 100! :')) #
                if guess > 100:
                    print('Not a valid guess')
                    continue
                elif guess < 1:
                    print('Not a valid guess')
                    continue
                elif True:
                    break                                                       # Check for valid input
            except ValueError:                                              #
                print('Not a valid guess')                                  #


        if guess > n:               #
                print('Too high!')  #
        elif guess < n:             # checks guess to n
                print('Too low!')   #
        elif guess == n:            #
                print('You got it!')#
                break
     
    
def main():
    guessing_game()

if __name__ == "__main__":
    main()

    


