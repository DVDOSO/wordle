from colorama import Fore
from time import sleep
from sys import stdout
from random import randint

words = ["alien", "bears", "crust"]
word = words[randint(0, len(words))]
guessed = False
guesses = 0

while guesses < 5:
  guess = input("Enter your guess: ")
  guess = guess.lower()
  if len(guess) != 5:
    print("Make sure to enter a 5 letter word!")
    continue
  if guess == word:
    guessed = True
    for letter in guess:
      sleep(0.2)
      stdout.write(Fore.GREEN + letter + Fore.WHITE)
      stdout.flush()
    print()
    break
  for j in range(5):
    if word[j] == guess[j]:
      sleep(0.2)
      stdout.write(Fore.GREEN + guess[j])
      stdout.flush()
    elif guess[j] in word:
      sleep(0.2)
      stdout.write(Fore.YELLOW + guess[j])
      stdout.flush()
    else:
      sleep(0.2)
      stdout.write(Fore.WHITE + guess[j])
      stdout.flush()
  guesses += 1
  print(Fore.WHITE)

if guessed:
  print("Congrats! You guessed the word!")
else:
  print("Better luck next time!")
  print("The word was", word)