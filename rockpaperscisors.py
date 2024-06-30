import random
your_action= input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
system_action = random.choice (possible_actions)                                                                             
print(f"\nYou chose {your_action}, computer chose {system_action}.\n")
if your_action == system_action:
  print(f"Both players selected {your_action}. It's a tie!")
elif your_action == "rock":
 if system_action == "scissors":
   print("Rock smashes scissors! You win!")
 else:
   print("Paper covers rock! You lose.")
elif your_action == "paper":
 if system_action == "rock":
     print("Paper covers rock! You win!")
 else:
  print("Scissors cuts paper! You lose.")
elif your_action == "scissors":
  if system_action == "paper":
   print("Scissors cuts paper! You win!")
  else:
   print("Rock smashes scissors! You lose.")