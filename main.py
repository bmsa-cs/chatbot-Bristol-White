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
  else:
    print("Ah,",str(age),"is a good age!")
  time.sleep(0.5)


if __name__ == "__main__":
  main()
  t = input("Run pytest? (y/n)").lower()
  if t == 'y':
    run_tests()