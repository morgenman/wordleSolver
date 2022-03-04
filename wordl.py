# Dylan Morgen 2022
# 
# Not my best work (it was written in an hour or two), but hey it works.
#


from time import sleep
from getch import getch
import os

# Global variables all functions pull from 
has = []  # array storing which letters are confirmed to be in the word
banned = [] # array storing which letters are confirmed NOT in the word
confirmed = {} # dictionary: <key=index, value=letter> (stores where correct letters are)
notHere = {} # dictionary: <key=index, value=letter> (where a letter is not)
guess = "" # empty initialization

# Word List
with open('words.txt') as f:
    lines = f.readlines() # parsed wordlist

# Terminal information
rows, columns = os.popen('stty size', 'r').read().split() # How many rows & columns does your terminal have?
  
def main():
  # import all the globals for convenience
  global has,banned,confirmed,notHere,guess,rows,columns,f

  print("\nWelcome to Wordle Solver by morgenman: ")
  guesses = 0
  
  while((confirmed.__len__()<5)&(guesses<6)):
     # increment guesses taken
    guesses+=1
    print() # newline

    # take user input
    guess = input("Input guess: ")

    # length checking
    while (guess.__len__()!=5):
      guess = input(guess.__len__().__str__() + " is an invalid length\nInput guess: ")
    
    # results of guess
    print("\nPlease tell me the results. Input 0 for grey, 1 for yellow, and 2 for green")
    for i in guess:
      print(" "+i+" ",end = '')
    results()
    if(confirmed.__len__()<5):
      print()  # newline

      # print available words left
      solve()

      # print what we know about the word
      printState()

    else: print("\nCongratulations! This game was solved in "+guesses.__str__()+" guesses!")
  
  # if we have less than five confirmed letters we didn't figure out the solution
  if(confirmed.__len__()<5): print("\nI'm sorry, better luck next time!")


# solve goes through the word list. It counts and prints possible words. 
def solve():
  # import all the globals for convenience
  global has,banned,confirmed,notHere,guess,rows,columns,f

  count = 0;
  # words stores the number of words that fits on the screen in one row
  words = int(int(columns)/8 - 1)

  # for each word in the word list
  for i in lines :
    i=i[0:5:1] # trim whitespace
    ok = True; # boolean for if a word could be the solution

    # invalid guess if it doesn't have all the letters in has
    for j in has:
      if (not i.__contains__(j)) : ok = False

    # invalid guess if it has letters in banned
    for k in banned:
      if (i.__contains__(k)) : ok = False

    # invalid guess if it doesn't the confirmed letters in the right place
    for l in confirmed:
      if (i[l-1]!=confirmed[l]) : ok = False

    # invalid guess if it has letters where it shouldn't
    for m in notHere:
      if (i[m-1]==notHere[m]) : ok = False


    if(ok):
      count+=1
      # print the word without a newline
      print(i,end='')

      # if we've written the number of words that fit in a row, newline
      if(count%words == 0) :print("")

      # tab character to line up words
      else :print("\t",end='')

  print("\nNumber of words: "+ count.__str__())


def printState() :
  # import all the globals for convenience
  global has,banned,confirmed,notHere,guess,rows,columns,f

  # print confirmed (letters we know the position of)
  for i in range(5):
    if(confirmed.__contains__(i+1)) : print("["+confirmed.get(i+1)+"]",end='')
    else : print("[ ]",end='')

  print() # newline
  print("Letters in the word: ",end='')

  # print the letters that we know are in the word
  if(has.__len__()>0):
    for j in range(has.__len__()-1) :print(has[j]+", ", end='')
    print(has[has.__len__()-1],end='')

  # print the letters we know are not in the word
  print("\nLetters not in the word: ", end='')
  if(banned.__len__()>0):
    for k in range(banned.__len__()-1) :print(banned[k]+", ", end='')
    print(banned[banned.__len__()-1])


def results() :
  # import all the globals for convenience
  global has,banned,confirmed,notHere,guess,rows,columns,f

  print()  # newline
  
  # for each letter, get the result
  for i in range(5):
    print('[',end='')
    
    # get a single character (unicode is due to getch weirdness)
    input = getch().decode('utf-8')
    # input validation
    while ((input!='1')& (input!='2')&(input!='0')) : 
      input = getch().decode('utf-8')

    # print without a newline
    print(input,end='')
    
    # convert green yellow grey information to appropriate data structures
    if (input == '1'):
        if not guess[i] in has : has.append(guess[i])
        notHere[i+1]=guess[i]
    elif (input == '2'):
        confirmed[i+1]=guess[i]
    elif (input == '0'):
        if not guess[i] in banned : banned.append(guess[i])

    # necessary to flush since we were capturing by character and now we are not
    print(']',end='', flush=True)
  print() # newline

# run main()
main()
