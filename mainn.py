import random
Main_List = ["stone", "paper", "scissors"]
print("\nHey! Welcome to Stone, Paper and Scissors!!\n")
print("Here is the menu you can access (Enter the number assosiated with your choice.)")
l = 0
k = open("score_swg.txt", "r")
try:
    p = int(k.read())
    l =1
    k.close()


except:
    k.close()
    f = open("score_swg.txt", "w")
    if l == 0:
        f.write("0")
    f.close()

while True:
    print("1) Rules\n2) Play\n3) Exit")

    a = int(input())

    if a == 1:
        print('Here are the rules :\n')
        print("Com'on You already know the rules for sps ya!\n")

    elif a == 2:
        score = 0
        i = 1
        print("\n***STARTING GAME***\n")
        rounds = int(input("How many rounds do you want to play? : "))
        print("\nType : \ns for stone\np for paper\nsc for scissor\n")
        while i <= rounds:
            print("\n Stooone...paperrrr...and scissorss..\n")
            b = input()
            choice = random.choice(Main_List)

            if b == "s" and choice == "stone" or b == "p"and choice == "paper" or b == "sc" and choice == "scissors":
                print(f"It's a draw! we both chose {choice}\n" )
                print(f"Your score is : {score}")

            elif b == "s" and choice == "paper":
                print(f"You lose! I chose {choice}")
                print(f"Your score is : {score}")

            elif b == "s" and choice == "scissors":
                score += 1
                print(f"You Won! I chose {choice}")
                print(f"Your score is : {score}")

            elif b == "p" and choice == "scissors":
                print(f"You lose! I chose {choice}")
                print(f"Your score is : {score}")

            elif b == "p" and choice == "stone":
                score += 1
                print(f"You Won! I chose {choice}")
                print(f"Your score is : {score}")

            elif b == "sc" and choice == "stone":
                print(f"You lose! I chose {choice}")
                print(f"Your score is : {score}")

            elif b == "sc" and choice == "paper":
                score += 1
                print(f"You Won! I chose {choice}")
                print(f"Your score is : {score}")

            elif b != "s" and b != "p" and b != "sc":
                print('Wrong input!\n')
                continue

            i +=1

        f = open("score_swg.txt", "r")
        m = int(f.read())
        f.close()



        if m < score:
            f = open("score_swg.txt", "w")
            print("\nNEW HIGH SCORE!!")
            print(f"Previous score was : {m}")
            f.write(f"{score}")
            f.close()
        print("\nThanks for playing!!\n")
        print(f"Your total score is : {score} \n")
    elif a == 3:
        break

    else:
        print('Wrong Input!!')
        



