# print('welcome to roll a dice game')
# Very Basic
import random
choice = input('Roll a dice ? (y/n)').lower()
while True:
    if(choice =='y') :
        dice = random.randint(1,6)
        print(f'Woah! you got \"{dice}\"')
        break
    elif choice=='n':
        print('thank you !')
        break
    else:
        print('invalid choice')
        