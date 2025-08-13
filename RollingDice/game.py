# print('welcome to roll a dice game')
# Very Basic
import random
while True:
    choice = input('Roll a dice ? (y/n)').lower()
    if(choice =='y') :
        dice = random.randint(1,6)
        print(f'Woah! you got \"{dice}\"')
        
    elif choice=='n':
        print('thank you !')
        break
    else:
        print('invalid choice')
        