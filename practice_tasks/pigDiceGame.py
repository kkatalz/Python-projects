import random
from termcolor import colored

def main():
    current_score = 0
    players = [1, 2]
    players_scores = {players[0]: 0, players[1]: 0}
    
    
    while current_score != 100:
        for player in players:
            print(f"\nPlayer {player}'s turn")

            while True:
                random_dice_points = random.randint(1, 6)
                print(f"You rolled a {random_dice_points}")

                if random_dice_points == 1:
                    players_scores[player] = 0
                    break
                
                else:
                    players_scores[player] += random_dice_points

                    roll_again_answer = input("Roll again? (y/n): ").lower()
                    if roll_again_answer == "y":
                         continue 
                    else: break

            current_score = players_scores[player]
            print(colored(f"\nYou scored {current_score} points this turn", 'light_magenta'))

            if str(player) == "1":
                next_player = 2
                print(colored(f"Current scores: Player {player}: {current_score}, {next_player}: {players_scores[next_player]}", 'light_green'))
            else:
                next_player = 1
                print(colored(f"Current scores: Player {next_player}: {players_scores[next_player]}, {player}: {current_score}", 'light_green'))


if __name__ == "__main__":
    main()