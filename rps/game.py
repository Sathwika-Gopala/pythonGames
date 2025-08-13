#Rock Paper Scissors
#Basic
import random
choices = ('r', 'p', 's')
fullNames = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
while True:
    userChoice = input('Rock, Paper or Scissors? (r/p/s):').lower()
    compChoice = random.choice(choices)
    if(userChoice not in choices and userChoice!='x'):
        print('invalid choice')
    elif(userChoice=='x'):
        break
    else:
        print(f'User\'s choice : {fullNames[userChoice]}')
        print(f'Computer\'s choice: {fullNames[compChoice]}')
    if(userChoice=='r' and compChoice=='p' or userChoice=='p' and compChoice=='s' or userChoice=='s' and compChoice=='r'):
        print('Better Luck Next Time! Computer won!')
    elif(compChoice==userChoice):
        print('Tie!')
    else:
        print('Congratulations! You Won!')
        
    print('click \'x\' to quit')