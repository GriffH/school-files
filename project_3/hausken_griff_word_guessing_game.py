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
    if lives == 0:
        global win
        win = False 
        print("You lose :(")

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
       if check not in word_list:
           life_lose()
           return

       for x in word_list:
           if check == x:
               if check not in correct:
                   correct.append(check)

def correct_guesses_display():
    print("Correct guesses so far: ", end="")
    for a in range(len(correct)):
       print(correct[a], ", ", sep="", end="")
    print()


def display():
    word_list = []
    word_list[:0] = word
    for a in word_list:
        if a in correct:
            print(a, " ", end="", sep="")
        else:
            print("_ ", end="")

def wincon():
    word_list = []
    word_list[:0] = word
    c = list(set(correct))
    w = list(set(word_list))
    if c == w:
        print("You Win!")
        global win
        win = False 


global win
win = True
def game():
    clear()
    getword()
    display()
    while win:
        get_guess()
        clear()
        check_guess(guess)
        display()
        life_counter()
        correct_guesses_display()
        wincon()


while True:
    game()
    play_again = input("Do you want to play again? y/n:")
    if play_again == "y":
        continue
    else:
        break


