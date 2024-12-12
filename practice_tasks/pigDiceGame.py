import random
from termcolor import colored
import sys
print(sys.path)

players = [1, 2]
first_player = players[0]
second_player = players[1]

players_scores = {first_player: 0, second_player: 0}
stop_game_for_player_number = 1


def player_score_per_game(player):
    
    print(f"\nPlayer {player}'s turn")
    while True:
        random_dice_points = random.randint(1, 6)
        print(f"You rolled a {random_dice_points}")

        if random_dice_points == stop_game_for_player_number:
            players_scores[player] = 0
            break
        
        else:
            players_scores[player] += random_dice_points
            roll_again_answer = input("Roll again? (y/n): ").lower()
            if roll_again_answer == "y":
                continue 
            else: break

    current_player_score = players_scores[player]
    print(colored(f"\nYou scored {current_player_score} points this turn", 'light_magenta'))
    return current_player_score

def curent_players_scores(player, current_player_score):

    if player == first_player:
        next_player = second_player
        print(colored(f"Current scores: Player {player}: {current_player_score}, {next_player}: {players_scores[next_player]}", 'light_green'))
    
    else:
        previous_player = first_player
        print(colored(f"Current scores: Player {previous_player}: {players_scores[previous_player]}, {player}: {current_player_score}", 'light_green'))

def main():
    
    current_player_score = 0
    winner_score = int(input("\nEnter the points player must get to win: "))
    
    while current_player_score < winner_score:

        for player in players:

            if current_player_score >= winner_score: break

            current_player_score = player_score_per_game(player)
            curent_players_scores(player, current_player_score)
    
    print(colored(f"Player {player} wins!", 'light_green'))


if __name__ == "__main__":
    main()