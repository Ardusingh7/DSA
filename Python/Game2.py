import time
import random

while True:

    print("Bot: Wanna play a game? (Y/N)")
    ques=input("You: ")
    if ques.upper()=="Y":
        print("Bot: Your name please?")
        name=input("You: ")
        print("Bot: {}, so much you wanna bet?".format(name))
        money=int(input("You: "))

        x=random.randint(1,12)
        print("Bot: Enter a number b/w (1-12)")
        y=int(input("You: "))

        if x<7 and y<7:
            print("Bot: You won and got {}".format(2*money))
        elif x>7 and y>7:
            print("Bot: You won and got {}".format(2*money))
        elif x==7 and y==7:
            print("Bot: LUCKY 7!")
            print("Bot: You won and got {}".format(3*money))
        else:
            print("Bot: You lost!")

    elif ques.upper()=="N":
        print("Bot: Nevermind :)",end=" ")
        time.sleep(2)
        print("You suck anyways...")
        break
    else:
        print("Bot: Wrong imput :/")
        print()
        continue