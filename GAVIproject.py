import random

#Creating list of cups to be randomize later
Cups = ['Cup1','Cup2','Cup3']
Play_game = True
Answer = random.choice(Cups)

while Play_game:
    #function for guessing what cup where the ball is hidden
    print("\nIn these three cups where is the ball hiding?")
    print("In which cup do you think the is? ")
    Answer_cup = input("Cup1, Cup2, Cup3? ")

    while Answer_cup not in "'Cup1Cup2Cup3":
        Answer_cup = input("Cup1, Cup2, Cup3")

    Ball_cup = Answer
    #aIf else statement for the winning condition
    if Answer_cup == Ball_cup:
        print("\nYou have Guessed right, You Win!")
    else:
        print("\nYou have Guessed incorrectly", "\nThe Ball was in ", Ball_cup)

    #Play again loop
    play_again = input("\nIf you'd like to play again, please type 'yes': \n")
    Answer1 = random.choice(Cups)
    if play_again == "yes":
        Answer = Answer1 #This re-shuffle the cup with the ball
        continue
    else:
        break