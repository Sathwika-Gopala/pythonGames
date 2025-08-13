import random
num = random.randint(1,100)
while True:
    try:
        guess = int (input('Guess the number between 1 and 100:'))
        if(1<=guess<=100):
            if(guess>=num+10):
                print('Too High!')
                
            elif(guess>num and guess<num+10):
                print('High!')
                
            elif(guess<=num-10):
                print('Too low!')
                
            elif(guess<num and guess>num-10):
                print('low!')
                
            elif(guess==num):
                print('Hurray! You guessed the number correctly. Congratulations!!')
            break
    except ValueError:
        print('invalid guess')