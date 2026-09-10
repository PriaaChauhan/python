import random
jackpot = random.randint(1, 100)

num = int (input("Guess the number between 1 and 100: "))
counter = 1

while num != jackpot:
    if num < jackpot :
        print ("Too low")
    else :
        print ("Too high")
    
    num = int (input("Guess  again: "))
    counter += 1
    
print(f"Congratulations! You guessed the  jackpot number {jackpot} in {counter} attempts.")