import random
import os

    

global correct
correct = []


global lives
lives = 9

global guessed
guessed = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def getword():
    lines  = open('wordlist.txt').read().splitlines()
    myline = random.choice(lines)
    global word
    word = myline
    #word = "hello"
    word = word.strip() 

        
def life_counter():
    global lives
    print("           Tries remaining: ",lives)

def life_lose():
    global lives
    lives -= 1
    print("           Tries remaining: ",lives)

def get_guess():
    while True:
        global guess
        guess = input("Guess a letter!:")
        if guess.isalpha() == 1:
            if len(guess) == 1:
                break
            else:
                print("Please enter only one letter.")
                continue
        else:
            print("Please enter only letters.")
            continue
        

def check_guess(check):
       word_list = []
       word_list[:0] = word
       if check in guessed:
           print("Already guessed")
           return
       guessed.append(check)
       for x in word_list:
           if check == x:
               if check not in correct:
                   correct.append(check)

def correct_guesses_display():
    print("Correct guesses so far: ", end="")
    for a in range(len(correct)):
       print(correct[a], ", ", sep="")


def display():
    word_list = []
    word_list[:0] = word
    for a in word_list:
        if a in correct:
            print(a, " ", end="", sep="")
        else:
            print("_ ", end="")

def win():
    word_list = []
    word_list[:0] = word
    c = list(set(correct))
    w = list(set(word_list))
    if c == w:
        print("You Win!")
        return True
    return
        

def play_again():
    play_again = input("Play again? y/n: ")
    if play_again == "y":
        return True
    elif play_again == "n":
        return False
        

clear()
getword()
life_counter()
while True:
    display()
    life_counter()
    correct_guesses_display()
    win()
    if win() == True:
        play_again()
        if play_again == True:
            continue
        elif play_again == False:
            break
    get_guess()
    check_guess(guess)
    clear()
