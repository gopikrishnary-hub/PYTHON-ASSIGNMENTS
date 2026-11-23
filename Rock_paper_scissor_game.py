print("Welcome to Rock Paper Scissor game")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
import random
your_choice = int(input('what would you like to choose? for "Rock" - type-0,for "paper" type-1 and for "scissor" type-2\n'))
computer_choice = random.randint(0,2)
print(f"your choice is :{your_choice},\ncomputer_choice is :{computer_choice}")
if your_choice == computer_choice:
    print("Draw")
elif your_choice == 0 and computer_choice == 1:
    print("You Lose")
    print(paper)
elif your_choice ==0 and  computer_choice == 2:
    print("You Win")
    print(rock)
elif your_choice ==1 and computer_choice ==0:
    print("You win ")
    print(paper)
elif your_choice == 1 and computer_choice == 2:
    print("You Lose")
    print(scissors)
elif your_choice == 2 and computer_choice == 0:
    print("You lose")
    print(rock)
elif your_choice == 2 and computer_choice == 1:
    print("you win")
    print(scissors)
else:
    print("you typed an invalid option so you lose the game ")
