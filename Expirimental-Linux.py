import os
import random
import time

from english_words import get_english_words_set

#List
word_list = list(get_english_words_set(['web2'], lower=True))
#Extras
word_list.append("pneumonoultramicroscopicsilicovolcanoconiosis")
word_list.append("hippopotomonstrosesquippedaliophobia")
word_list.append("pseudopseudohypoparathyroidism")
word_list.append("floccinaucinihilipilification")
word_list.append("aequeosalinocalcalinoceraceoaluminosocupreovitriolic")

#Variables
lives = 6
picked = []
valid = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
difficulties = ["easy", "normal", "hard", "extreme", "impossible"]
difficulty = ""
reset_list = []
word = ""
answer = ""
guess = ""
not_valid = 0
again = ""
yes = ["yes", "y"]
no = ["no", "n"]

#Functions
def initiate_difficulty(): #DONE
  global answer
  while True:
    print("Welcome to hangman!\n")
    difficulty = input("Do you want to play easy, normal, hard, extreme, or impossible mode?\n> ")
    difficulty = difficulty.lower().strip()
    if difficulty not in difficulties:
      invalid(initiate_difficulty)
      initiate_difficulty()
    else:
      print("loading...\n")
      for word in word_list:  
        if (difficulty == "easy" and len(word) <= 5) or (difficulty == "normal" and len(word) >= 7 and len(word) <= 11) or (difficulty == "hard" and len(word) >= 13 and len(word) <= 16) or (difficulty == "extreme" and len(word) >= 18 and len(word) <= 22) or (difficulty == "impossible" and len(word) >= 24):
          reset_list.append(word)    
      answer = random.choice(reset_list)
      os.system("clear")
      break

def guessing(): #DONE
  global not_valid, word, lives
  word = "".join([i if i in picked else "_" for i in answer])
  while True:
    print("Welcome to hangman! Try to guess the word before you run out of lives!\n")
    print(f"already guessed: {', '.join(sorted(picked))}\n")
    print(f"{word}\n")   
    guess = input("Guess a letter\n> ")
    print()
    if guess in picked:
      print(f"You already guessed {guess}.")
      time.sleep(1)
      os.system("clear")
      guessing()
    guess = guess.lower().strip()  
    picked.append(guess)
    for letter in guess:
      if letter not in valid:
        not_valid += 1
    if not_valid >= 1:
      invalid(guessing) 

    if len(guess) != 1 and guess == answer:
      os.system("clear")
      print("Welcome to hangman! Try to guess the word before you run out of lives!\n")
      print(f"already guessed: {', '.join(sorted(picked))}\n")
      print(f"{answer}\n")   
      print(f"Guess a letter\n> {guess}")
      print()
      print(f"You won with {lives} {'lives' if lives != 1 else 'life'} left!\n")
      play_again()
    elif len(guess) != 1:
      lives -= 1
      if lives == 0:
        print(f"You lost. The word was {answer}.\n")
        play_again()
      else:
        print(f"\n{guess} is incorrect. You have {lives} {'life' if lives == 1 else 'lives'} left\n")  
        time.sleep(1)
        os.system("clear")
        guessing()    
    elif guess in answer:
      word = "".join([i if i in picked else "_" for i in answer])
      print("\nCorrect!\n")
      if "_" not in word:
        word = "".join([i if i in picked else "_" for i in answer])
        os.system("clear")
        print("Welcome to hangman! Try to guess the word before you run out of lives!\n")
        print(f"already guessed: {', '.join(sorted(picked))}\n")
        print(f"{word}\n")   
        print(f"Guess a letter\n> {guess}")
        print()
        print(f"You won with {lives} {'lives' if lives != 1 else 'life'} left!\n")
        play_again()
      else:
        time.sleep(1)
        os.system("clear")
        guessing()
    else:
      lives -= 1
      if lives == 0:
        print(f"You lost. The word was {answer}.\n")
        play_again()
      else:
        print(f"\n{guess} is incorrect. You have {lives} {'life' if lives == 1 else 'lives'} left\n")  
        time.sleep(1)
        os.system("clear")
        guessing()    
        
def invalid(function): #DONE
  print("invalid input")
  time.sleep(1)
  os.system("clear")
  function()
  
def play_again(): #DONE
  again = input("Do you want to play again?\n> ")
  again = again.lower().strip()
  if again in yes:
    time.sleep(1)
    os.system("clear")
    main()
  elif again in no:
    print("\nThanks for playing!")
    quit()
  else:
    invalid(play_again)
  
def main(): 
  global picked, word, reset_list
  picked = []
  word = ""
  reset_list = []
  initiate_difficulty()
  guessing()
  play_again()

main()