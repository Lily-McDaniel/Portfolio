#dice roll game
import random
nChips = 10

print("Hello, welcome to roulette!")
bet = int(input("You currently have "+str(nChips)+". How many chips do you want to bet?"))
if (bet > nChips):
  print("This bet is too high. You only have " + str(nChips) + " chips.")
else:
  print("You are placing a bet of " + str(bet)  + " chips.")
bet1 = int(input("Do you want to bet on black or red? (b/r)"))
if (bet1 == "r"):
  print("You are betting " + str(bet) + " chips on red.")
else:
  print("You are betting " + str(bet) + " chips on black.")

for i in range(spins):
    x = random.randint(1,6)
    guess = int(input("Take a guess 1-6:"))
    if guess == x:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You earned 6 points")
        points += 6
    else:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You lost 1 point")
        points -= 1

print("Final score =", points)

import random

rolls = int(input("How many rolls do you want to play?"))
points = 0

for i in range(rolls):
    x = random.randint(1,6)
    guess = int(input("Take a guess 1-6:"))
    if guess == x:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You earned 6 points")
        points += 6
    else:
        print("Your guess was", guess)
        print("The correct roll was", x)
        print("You lost 1 point")
        points -= 1

print("Final score =", points)

#version 3
import random
nChips = 10

print("Hello, and welcome to roulette!")
bet = int(input("You currently have "+str(nChips)+". How many chips do you want to bet?"))
if (bet > nChips):
  print("This bet is too high. You only have " + str(nChips) + " chips.")
else:
  print("You are placing a bet of " + str(bet)  + " chips.")

bet1 = int(input("Do you want to bet on black or red? (1/2)"))
for i in range(bet1):
    x = random.randint(1,2)

    if bet1 == x:
        print("You bet on black.")
        print("YAY. You doubled your money!")
        bet = bet*2
        nChips = nChips + bet
    else:
        print("You bet on red.")
        print("You lost your bet :'(. Try again!")
        nChips = nChips-bet

print("Final score =", nChips)

#version 4
import random
nChips = 0

print("Hello, and welcome to roulette!")
bet = int(input("How many chips do you want to place per bet?"))
spins = int(input("How many bets do you want to place?(1/2/3/4/5)"))

for i in range(spins):
    x = random.randint(1,2)
    bet1 = int(input("Do you want to bet on black or red? (1/2)"))
    if bet1 == x:
        print("You bet on black.")
        print("YAY. You doubled your bet!")
        nChips = nChips + 2*bet
    else:
        print("You bet on red.")
        print("You lost your bet :'(. Try again!")
        nChips = nChips-bet

print("Total =", nChips)

#whole game
import random
player = input("Welcome to Game Master 4! Do you want to play? (y/n)")

#Rashon
def blackjack():
    user = [];
    comp = [];
    def gameplay():
        user.append(random.randint(1,10));
        comp.append(random.randint(1,10));
        print(user);
        print(comp);
        stance = input("Hit or stay?");
        while stance.lower() != "stay":
            user.append(random.randint(1,10));
            updateSum(user);
            #print(user);
            stance = input("Hit or stay?");
        print("User score: " + str(updateSum(user)));
        compGameplay();

    def compGameplay():
        if updateSum(user) > 21:
                updateSum(comp);
        elif updateSum(user) <= 21:
            while updateSum(comp) < updateSum(user):
                comp.append(random.randint(1,10));
                print("Comp score: " + str(updateSum(comp)));
                print(comp);
        else:
            doNothing();

    def updateSum(cards):
        total = 0;
        bust = False;
        if total <= 21:
            for x in range(len(cards)):
                total = total + cards[x];
            if total > 21:
                total = 99;
        print(total);
        return total;
    def doNothing():
        1+1;
    def main():
        gameplay();
    main();

def guessColor():
    user_score = 0
    colors = ['red', 'blue', 'black', 'pink']
    x = random.randint(0,len(colors)-1)
    guess = input('Guess a color Red, Blue, Black, Pink: ')

    for color in colors[x]:
        if guess != colors[x]:
            print('Try again!')
            guess = input('Guess a color Red, Blue, Black, Pink: ')
            user_score -= 1
        elif guess == colors[x]:
            user_score += 6
            break

    print('Congrats, you win! Color was: ' + colors[x])
    print('Your final score is {} '.format(user_score))
    cont = input("Do you want to keep playing? (y/n)")
    if cont == "y":
        ready_player1()
 #Chang Liu
def rockPaperSci():
    user = input("Enter a choice (rock, paper, scissors): ")
    computer = ["rock", "paper", "scissors"]
    computer = random.choice(computer)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
           if computer == "scissors":
            print("Rock smashes scissors! You win!")
           else:
            print("Paper covers rock! You lose.")
            ready_player1()
    elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
    elif user == "scissors":
            if computer == "paper":
                    print("Scissors cuts paper! You win!")
            else:
                    print("Rock smashes scissors! You lose.")

#Lily
def diceroll():
    rolls = int(input("How many rolls would you like to play?"))
    points = 0

    for i in range(rolls):
        x = random.randint(1,6)
        guess = int(input("Guess 1-6:"))
        if guess == x:
            print("Your guess was", guess)
            print("The correct roll was", x)
            print("You earned 6 points")
            points += 6
        else:
            print("Your guess was", guess)
            print("The correct roll was", x)
            print("You lost 1 point")
            points -= 1

    print("Final score =", points)

def ready_player1():
    player = 0
if player == "n":
    print("Bye, see you next time!")
elif player == "y":
    print("Games:\n 1. Coin Flipper\n 2. Guess my Color")
    game_choice = int(input("Which game do you want to play? Blackjack, Guess Color, Rock Paper Scissors, Dice Roll (1/2/3/4): "))
if game_choice == 1:
    blackjack()
elif game_choice == 2:
    guessColor()
elif game_choice == 3:
    rockPaperSci()
elif game_choice == 4:
    diceroll()

#v2
import random


#Rashon
def blackjack():
    user = [];
    comp = [];
    def gameplay():
        user.append(random.randint(1,10));
        comp.append(random.randint(1,10));
        print("User score: " + str(updateSum(user)));
        print("Comp score: " + str(updateSum(comp)))
        stance = input("Hit or stay?");
        while stance.lower() != "stay":
            user.append(random.randint(1,10));
            print("User score: " + str(updateSum(user)));
            #print(user);
            stance = input("Hit or stay?");
        print("User score: " + str(updateSum(user)));
        compGameplay();

    def compGameplay():
        if updateSum(user) > 21:
                updateSum(comp);
        elif updateSum(user) <= 21:
            while updateSum(comp) < updateSum(user):
                comp.append(random.randint(1,10));
                print("Comp score: " + str(updateSum(comp)));
                print(comp);
        else:
            doNothing();

    def updateSum(cards):
        total = 0;
        bust = False;
        if total <= 21:
            for x in range(len(cards)):
                total = total + cards[x];
            if total > 21:
                total = 99;
        print(total);
        return total;
    def doNothing():
        1+1;
    def main():
        gameplay();
    main();
#Oksana
def guessColor():
    user_score = 0
    colors = ['red', 'blue', 'black', 'pink']
    x = random.randint(0,len(colors)-1)
    guess = input('Guess a color Red, Blue, Black, Pink: ')

    for color in colors[x]:
        if guess != colors[x]:
            print('Try again!')
            guess = input('Guess a color Red, Blue, Black, Pink: ')
            user_score -= 1
        elif guess == colors[x]:
            user_score += 6
            break

    print('Congrats, you win! Color was: ' + colors[x])
    print('Your final score is {} '.format(user_score))
 #Chang Liu
def rockPaperSci():
    user = input("Enter a choice (rock, paper, scissors): ")
    computer = ["rock", "paper", "scissors"]
    computer = random.choice(computer)
    print(f"\nYou chose {user}, computer chose {computer}.\n")

    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "rock":
        if computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user == "paper":
            if computer == "rock":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
    elif user == "scissors":
            if computer == "paper":
                    print("Scissors cuts paper! You win!")
            else:
                    print("Rock smashes scissors! You lose.")

#Lily
def diceroll():
    rolls = int(input("How many rolls would you like to play?"))
    points = 0

    for i in range(rolls):
        x = random.randint(1,6)
        guess = int(input("Guess 1-6:"))
        if guess == x:
            print("Your guess was", guess)
            print("The correct roll was", x)
            print("You earned 6 points")
            points += 6
        else:
            print("Your guess was", guess)
            print("The correct roll was", x)
            print("You lost 1 point")
            points -= 1

    print("Final score =", points)


def ready_player1():
    player = input("Welcome to Game Master 4! Do you want to play a game? (y/n)")
    while player == "y":
            game_choice = int(input("Which game do you want to play? Blackjack, Guess Color, Rock Paper Scissors, Dice Roll (1/2/3/4): "))
            if game_choice == 1:
                blackjack()
            elif game_choice == 2:
                guessColor()
            elif game_choice == 3:
                rockPaperSci()
            elif game_choice == 4:
                diceroll()
            player = input("Do you want to keep playing? (y/n)")
    else:
        print("Game Over!")
ready_player1()
