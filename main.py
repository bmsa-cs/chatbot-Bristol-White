"""
Chatbot
Author: Bristol White
Period/Core: 2

"""

import os
import importlib.util
import time
import random
from datetime import date

def run_tests():
  """
  This function will check for the pytest module
  before calling it to run the included tests.py
  """
  if importlib.util.find_spec('pytest') is None: # Check if pytest is installed
    os.system('python3 -m pip install -q pytest')

  command = "python3 -m pytest --tb=line -v -s tests.py"
  print(command)
  os.system(command)

def main():
  """This function contains all code for the chatbot."""
  name = input("Yo, I'm ChatBuddy, what's your name?")
  time.sleep(0.5)
  print("Nice to meet you", name,"!")
  age = int(input("So how old are ya?"))
  if age == 16:
    print("Ah,",str(age),"is a good age! Old enough to drive, nice!")
  elif age == 15:
    print("Ah,",str(age),"is a good age! Old enough to get your drivers permit, nice!")
  elif age >= 20:
    print("Ah,",str(age),"is a good age! Old enough to drink and drive! \n(But don't combine those two things please!)")
  else:
    print("Ah,",str(age),"is a good age!")
  time.sleep(0.5)
  print("Bet I can guess what year you were born.")
  time.sleep(0.3)
  year = 2021 - age
  today = date.today()
  if year <= 1800:
    print("Hey, wait a minute, you shouldn't be alive!")
  else:
    print("If today is",today,"...")
    print("Let's see here... according to my calculations you were born in", year,)
  answer = input("Was I correct? (y/n)")
  if answer == "y":
    print("Easy, a robot never fails!")
  if answer == "n":
    answer_two = input("Darn, was I close at least? (yy/nn)")
    if answer_two == "yy":
      print("Well that's good! Robots aren't perfect afterall!")
    if answer_two == 'nn':
      print("Ah, that's unlucky. Robots aren't perfect.")
  mood = input("So anyways, how are you feeling today?")
  if mood == "Good" or "Happy" or "Nice":
    print("I'm glad you're feeling", mood.lower() ,",that's good to hear!")
  else:
    print("Thanks for sharing", name ,"!")
  time.sleep(1)
  print("You know, I really wanna play a number game right now. Let's play \n\"Guess the Number!\"")
  answer_three = input("I'll think of a number between 1 and 100, and you have to guess it. \nReady? (y/n)")
  if answer_three == "y":
    number = random.randint(1,100)
    guess = input("Ok, guess the number! I'll give you 10 seconds to think.")
    time.sleep(10)
    if guess == number:
      print("Wow, you were correct! Nice job", name,"!")
    if guess != number:
      print("The number was:", number,". You were close at least!")
  if answer_three == "n":
    print("Sorry, but I'm not gonna take no for an answer!")
    number = random.randint(1,100)
    guess = input("Ok, guess the number! I'll give you 10 seconds to think.")
    time.sleep(5)
    if guess == number:
      print("Wow, you were correct! Nice job", name,"!")
    if guess != number:
      print("The number was:", number,". You were close at least!")
  time.sleep(1)
  print("Ok, I wanna get to know you better. I'm gonna ask you a series of questions, ok?")
  question = random.randint(1,5)
  if question == 1:
    answer_four = input("What is your favorite color?")
  elif question == 2:
    answer_four = input("Have you had any pets in the past?")
  elif question == 3:
    answer_four = input("Where were you born?")
  elif question == 4:
    answer_four = input("Do you have any hobbies?")
  elif question == 5:
    answer_four = input("Do you still feel", mood,"?")
  time.sleep(3)
  if answer_four == "Las Vegas":
    print("Oh wow, me too!")
  else:
    print("That's pretty interesting, thanks for sharing.")

if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()