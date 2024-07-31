import random

# save Ascii to vairables
rock_asscii ="""
    ______
---'  ____)
      (_____)
      (_____)
---__(____)
  """
paper_asscii = """
    ______
----'  ____)____
          ______)
          _______)
         _______)
---_________)
      """

scissors_asscii= """ 
    ______
----'  ____)____
        ________)
        _________)
        (___)
---_____(__)
      """
print ("Welcom to the Rock, Paper, Scissors game:")

help = input("Press Enter to continue or type (Help) for the rules: \n")

if help.lower() == "help":
  print("                   ********** RULES **********")
  print("                   1) You choose and the computer chooses")
  print("                   2) Rock smashes Scissors -> Rock wins")
  print("                   3) Scissors cut Paper -> Scissors win")
  print("                   4) Paper covers Rock -> Paper wins\n")

your_choise = input("\nEnter your choise (Rock, Paper, Scissors): ").lower()

if your_choise not in ["rock", "paper", "scissors"]:
  print ("\nInvalid choise")
  print ("please run the program again and choose rock, paper or scissors.")
  quit()

if your_choise == "rock":
  print (f"\nyour choise is: \n\n {rock_asscii}")
if your_choise == "paper":
  print (f"\nyour choise is: \n\n {paper_asscii}")
if your_choise == "scissors":
  print (f"\nyour choise is: \n\n {scissors_asscii}")

computer_choise = random.choice(["rock", "paper", "scissors"])
if computer_choise == "rock":
  print (f"\ncomputer choise is: \n\n {rock_asscii}")
if computer_choise == "paper":
  print (f"\ncomputer choise is: \n\n {paper_asscii}")
if computer_choise == "scissors":
  print (f"\ncomputer choise is: \n\n {scissors_asscii}")

# the results
if your_choise == computer_choise:
   print ("It's a tie!")
if your_choise == "rock" and computer_choise == "paper":
   print ("you lose!")

if your_choise == "paper" and computer_choise == "rock":
   print ("you win!")

if your_choise == "paper" and computer_choise == "scissors":
   print ("you lose!")

if your_choise == "scissors" and computer_choise == "paper":
  print ("you win!")

if your_choise == "scissors" and computer_choise == "rock":
   print ("you lose!")

if your_choise == "rock" and computer_choise == "scissors":
   print ("you lose!")