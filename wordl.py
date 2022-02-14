from time import sleep
from getch import getch
with open('words.txt') as f:
    lines = f.readlines()

import os
rows, columns = os.popen('stty size', 'r').read().split()

has = []
banned = []
confirmed = {}
notHere = {}
  
def solve():
  count = 0;
  words = int(int(columns)/8 - 1)
  for i in lines :
    i=i[0:5:1]
    ok = 1;
    for j in has:
      if (not i.__contains__(j)) : ok = 0
    for k in banned:
      if (i.__contains__(k)) : ok = 0
    for l in confirmed:
      if (i[l-1]!=confirmed[l]) : ok =0
    for m in notHere:
      if (i[m-1]==notHere[m]) : ok =0
    if(ok):
      count+=1
      print(i,end='')
      if(count%words == 0) :print("")
      else :print("\t",end='')
  print("\nNumber of words: "+ count.__str__())


def printState() :
  for i in range(5):
    if(confirmed.__contains__(i+1)) : print("["+confirmed.get(i+1)+"]",end='')
    else : print("[ ]",end='')
  print("")
  print("Letters in the word: ",end='')
  if(has.__len__()>0):
    for j in range(has.__len__()-1) :print(has[j]+", ", end='')
    print(has[has.__len__()-1],end='')
  print("\nLetters not in the word: ", end='')
  if(banned.__len__()>0):
    for k in range(banned.__len__()-1) :print(banned[k]+", ", end='')
    print(banned[banned.__len__()-1])


def results() :
  print("")
  for i in range(5):
    print('[',end='')
    input = getch().decode('utf-8')
    while ((input!='1')& (input!='2')&(input!='0')) : 
      input = getch().decode('utf-8')
    print(input,end='')
    if (input == '1'):
        if not guess[i] in has : has.append(guess[i])
        notHere[i+1]=guess[i]
    elif (input == '2'):
        confirmed[i+1]=guess[i]
    elif (input == '0'):
        if not guess[i] in banned : banned.append(guess[i])
    print(']',end='', flush=True)
  print("")

    
print("\nWelcome to Wordle Solver by morgenman:\n ")

guesses = 0
guess = input("Please input your first guess: ")
while (guess.__len__()!=5):
  guess = input(guess.__len__().__str__() + " is an invalid length\nInput first guess: ")

print("\nPlease tell me the results. Input 0 for grey, 1 for yellow, and 2 for green")
for i in guess:
  print(" "+i+" ",end = '')
results()
solve()
printState()
guesses+=1

while((confirmed.__len__()<5)&(guesses<6)):
  guesses+=1
  print()
  guess = input("Input guess: ")
  while (guess.__len__()!=5):
    guess = input(guess.__len__().__str__() + " is an invalid length\nInput first guess: ")

  print("\nPlease tell me the results. Input 0 for grey, 1 for yellow, and 2 for green")
  for i in guess:
    print(" "+i+" ",end = '')
  results()
  if(confirmed.__len__()<5):
    solve()
    printState()
  else : print("\nCongratulations! This game was solved in "+guesses.__str__()+" guesses!")

if(confirmed.__len__()<5): print("\nI'm sorry, better luck next time!")

