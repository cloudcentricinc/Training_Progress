import random

highest = 1000
answer = random.randint(1,highest)
print(answer)   # TODO: Remove after testing
guess = 0
print("please guess number between 1 and {}:".format(highest))

while guess != answer:
    guess = int(input())

    if guess == 0:
        break
    if guess == answer:
        print("well done,you guessed it")
        break
    else:
        if guess < answer:
            print("please guess higher")
        else:
            print("please guess lower")
        #guess = int(input())
        ##       print("well done,you guessed it")
        #else:
         #   print("sorry, you have not guessed correctly")


