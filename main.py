"""
Chatbot
Author: Bristol White
Period/Core: 2

"""

import os
import importlib.util
import time
import random

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
  if age >= 16:
    print("Ah,",str(age),"is a good age! Old enough to drive, nice!")
  elif age == 16:
    print("Ah,",str(age),"is a good age! Old enough to get your drivers permit, nice!")
  elif age >= 21:
    print("Ah,",str(age),"is a good age! Old enough to drink and drive! (But don't combine those two things please!)")
  else:
    print("Ah,",str(age),"is a good age!")
  time.sleep(0.5)
  print("Bet I can guess what year you were born.")
  time.sleep(0.3)
  year = 2021 - age
  if year <= 0:
    print("Hey, wait a minute, you shouldn't be alive!")
  else:
    print("Let's see here... according to my calculations you were born in", year,)
  answer = input("Was I correct? (y/n)")
  if answer == "y":
    print("Easy, a robot never fails!")
  if answer == "n":
    answer_two = input("Darn, was I close at least? (y/n)")
    if answer_two == "y":
      print("Well that's good! Robots aren't perfect afterall!")
    if answer_two == 'n':
      print("Ah, that's unlucky. Robots aren't perfect.")
    else:
      print("Sorry, I don't quite understand what you said. Try again pelase!")
      answer_two = input("Darn, was I close at least? (y/n)")
      if answer_two == "y":
        print("Well that's good! Robots aren't perfect afterall!")
      if answer_two == 'n':
        print("Ah, that's unlucky. Robots aren't perfect.")
  else:
    print("Sorry, I don't quite understand what you said. Try again please!")
    answer = input("Was I correct? (y/n)")
    if answer == "y":
      print("Easy, a robot never fails!")
    if answer == "n":
      answer_two = input("Darn, was I close at least? (y/n)")
      if answer_two == "y":
        print("Well that's good! Robots aren't perfect afterall!")
      if answer_two == 'n':
        print("Ah, that's unlucky. Robots aren't perfect.")
      else:
        print("Sorry, I don't quite understand what you said. Try again pelase!")


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()