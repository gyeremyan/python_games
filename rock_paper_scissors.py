import random

print("Rock...")
print("Paper...")
print("Scissors...")

p1 = input("Player 1, make your move: ").lower()
rand_num = random.randint(1,3)
if rand_num == 1:
	computer = "rock"
elif rand_num == 2:
	computer = "paper"
else:
	computer = "scissors"
print(f"Computer plays {computer}")

if p1 == computer:
	print("its a tie!")
elif p1 == "rock":
	if computer == "scissors":
		print("player 1 wins")
	elif computer == "paper":
		print("player 2 wins")
elif p1 == "scissors":
	if computer == "rock":
		print("player 2 wins")
	elif computer == "paper":
		print == ("player 1 wins")
elif p1 == "paper":
	if computer == "rock":
		print("Player 1 wins")
	if computer == "scissors":
		print("computer wins")

else:
	print("something went wrong")
	
