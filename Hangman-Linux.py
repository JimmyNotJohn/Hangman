import os
import random
import time

from english_words import get_english_words_set

word_list = list(get_english_words_set(['web2'], lower=True))
word_list.append("pneumonoultramicroscopicsilicovolcanoconiosis")
word_list.append("hippopotomonstrosesquippedaliophobia")
word_list.append("pseudopseudohypoparathyroidism")
word_list.append("floccinaucinihilipilification")
word_list.append("aequeosalinocalcalinoceraceoaluminosocupreovitriolic")
while True:
  hard = input(
      "Do you want to play easy, normal, hard, extreme, or impossible mode?\n> "
  )
  difficulty = 0
  difficulties = ["easy", "normal", "hard", "extreme", "impossible"]
  lives = 6
  crazy = ""
  if hard.lower().strip() not in difficulties:
    print("Invalid input")
    time.sleep(1)
    os.system("clear")
    continue
  print("\nLoading...")
  if hard.lower().strip() == "easy":
    difficulty = 0
    break
  elif hard.lower().strip() == "normal":
    difficulty = 1
    break
  elif hard.lower().strip() == "hard":
    difficulty = 2
    break
  elif hard.lower().strip() == "extreme":
    crazy = "Extreme"
    difficulty = 3
    lives = 4
    break
  elif hard.lower().strip() == "impossible":
    crazy = "Ultimate"
    difficulty = 4
    lives = 1
    break

crazy_saucer = []
for x in word_list:
  if difficulty == 0 and len(x) <= 5:
    crazy_saucer.append(x)
  elif difficulty == 1 and len(x) >= 7 and len(x) <= 11:
    crazy_saucer.append(x)
  elif difficulty == 2 and len(x) >= 13 and len(x) <= 16:
    crazy_saucer.append(x)
  elif difficulty == 3 and len(x) >= 18 and len(x) <= 22:
    crazy_saucer.append(x)
  elif difficulty == 4 and len(x) >= 24:
    crazy_saucer.append(x)
time.sleep(1)
os.system("clear")


def reset():
  os.system("clear")
  if crazy != "":
    print(
        f"Welcome to {crazy} Hangman! Try to guess the word before you run out of guesses."
    )
  else:
    print(
        "Welcome to Hangman! Try to guess the word before you run out of guesses."
    )
  print()
  print(hidden)
  print()


answer = random.choice(crazy_saucer)
picked = []
hidden = "_" * len(answer)

if crazy != "":
  print(
      f"Welcome to {crazy} Hangman! Try to guess the word before you run out of guesses."
  )
else:
  print(
      "Welcome to Hangman! Try to guess the word before you run out of guesses."
  )
print()
print(hidden)
print()
while True:
  guess = input("Guess a letter:\n> ")
  if guess == answer:
    print("Correct!")
    print()
    time.sleep(1)
    if lives == 1:
      print(f"You won with {lives} life left!")
    else:
      print(f"You won with {lives} lives left!")
    break
  if guess in picked:
    print()
    print(f"You already guessed {guess}.")
    time.sleep(1)
    reset()
  else:
    picked.append(guess)
    if guess in answer:
      hidden = "".join([i if i in picked else "_" for i in answer])
      print()
      print("Correct!")
      time.sleep(1)
      reset()
      if "_" not in hidden:
        print(
            f"You won with {lives} {'life' if lives == 1 else 'lives'} left!")
        break
    elif guess not in answer and lives != 0:
      lives -= 1
      if lives != 0:
        print()
        print(f"{guess.capitalize()} is incorrect.")
        print(f"You have {lives} {'life' if lives == 1 else 'lives'} left.")
        time.sleep(1)
        reset()
      else:
        print()
        print(f"You ran out of lives. The word was {answer}.")
        break
    else:
      print()
      print(f"You ran out of lives. The word was {answer}.")
      break
