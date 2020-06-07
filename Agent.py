#Authors: Mert Doğan, Mert Günay.


import random #For generating random integers
import sys #sys for exit the program

#definitions
rock = "rock"
paper = "paper"
scissors = "scissors"

#definitions arrays for random selection
arr = [rock,paper,scissors]
arr1 = [rock,paper]
arr2 = [rock,scissors]
arr3 = [paper,scissors]

#counters for showing the result
counterAgent = 0
counterHuman = 0
draw = 0

#Game start screen
print("Welcome the Rock, Paper, Scissors Game!\n\n")
print("Moves: rock, scissors, paper\n")
print("For quit enter q\n\n")

#starting statistics (for human)
randm = random.randint(0, 1000)
if randm < 343:
    agent = paper

elif randm > 342 and randm < 701:
    agent = scissors
    
else:
    agent = rock

#the whole game
while True:
    #print(agent)
    move = input("Please make a move\n\n")  #human move input

    #exit the program
    if move == "q":
        print("Total Games: "+str(counterAgent+counterHuman+draw)
              +"\nComputer: "
              +str(counterAgent)+"\nHuman: "+str(counterHuman)
              +"\nDraw: "+str(draw))
        sys.exit(0)

    #draw situation
    if move == agent:
        print("Draw")
        agent = arr[random.randint(0,2)] #choose random move
        draw += 1 #counter for draw
        continue

    #human makes a move: rock
    if move == rock:

        #if agent choose scissors
        if agent == scissors:
            print("You win")
            counterHuman += 1  #counter for human score
            agent = paper   #against the human
            continue

        # if agent choose paper
        if agent == paper:
            print("You Lose")
            counterAgent += 1  #counter for agent score
            agent = arr3[random.randint(0,1)]  #choose random move except rock
            continue
            #######################

    # human makes a move: paper
    if move == paper:

        # if agent choose scissors
        if agent == scissors:
            print("You Lose")
            counterAgent += 1  #counter for agent score
            agent = arr2[random.randint(0,1)]  #choose random move except paper
            continue

        # if agent choose rock
        if agent == rock:
            print("You Win")
            counterHuman += 1  #counter for human score
            agent = scissors  #against the human
            continue
            #######################

    # human makes a move: scissors
    if move == scissors:

        # if agent choose paper
        if agent == paper:
            print("You win")
            counterHuman += 1  #counter for human score
            agent = rock       #against the human
            continue
        # if agent choose rock
        if agent == rock:
            print("You Lose")
            counterAgent += 1  #counter for agent score
            agent = arr1[random.randint(0,1)]  #choose random move except scissors



