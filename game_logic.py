import random

#define the list of expected moves for both player and ai
move_choices = ["rock", "paper", "scissors"]

#flag used for play_game()
game_state = True

#function to print a welcome message
def start_game():
	game_start_message = f"Welcome to rock paper scissors!"
	game_start_message += f"\n\nThe game choices are rock, paper, or scissors. "
	print(game_start_message)

#function to control game logic
def play_game():
    
    #variables to clean up win lose messsages
	win_message = "You win!"
	lose_message = "You lose!"

	#scores
	player_win_amount = 0
	opponent_win_amount = 0

	while game_state:	
        #choice a random choice from the list defined above
		opponent_choice = random.choice(move_choices)
		player_choice = input(f"\nInput a choice to play the game: ")
		
        #used to end gameplay
		if player_choice == "q":
			return False	
		else:
			if player_choice not in move_choices:
				print("That is not rock, paper or scissors please input one of those choices.")
			else:
				if player_choice == opponent_choice:
					print(f"The oppenent selected {opponent_choice}")
					print("It is a tie!")
				elif player_choice == "rock" and opponent_choice == "scissors":
					print(f"The oppenent selected {opponent_choice}")
					print(win_message)
					player_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")
				elif player_choice == "rock" and opponent_choice == "paper":
					print(f"The oppenent selected {opponent_choice}")
					print(lose_message)
					opponent_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")
				elif player_choice == "paper" and opponent_choice == "rock":
					print(f"The oppenent selected {opponent_choice}")
					print(win_message)
					player_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")
				elif player_choice == "paper" and opponent_choice == "scissors":
					print(f"The oppenent selected {opponent_choice}")
					print(lose_message)
					opponent_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")
				elif player_choice == "scissors" and opponent_choice == "paper":
					print(f"The oppenent selected {opponent_choice}")
					print(win_message)
					player_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")
				else:
					print(lose_message)
					opponent_win_amount += 1
					print(f"The score is Player: {player_win_amount} Oppoenet: {opponent_win_amount}")

	

	


#execute functions to start and play game. We set game state to play_game so that if false end.	
start_game()
game_state = play_game()