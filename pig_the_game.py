# in this game, a number of players (2-4) will roll the dice.  If they get a value of 1 they loose 
# their turn and all their points.  If not they continue to play.  They can also choose to stop their 
# turn and keep their points until the next turn.  Whoever gets 50 points first wins
import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2 - 4 players.")
    else:
        print("Invalid, try again.")

max_score = 50
# [0 for _ in range(players)]: This is a list comprehension, a concise way to create a list in Python. 
# 0: This is the value that you want to initialize each element of the list with. In this case, it's 0.
# for _ in range(players): This part of the list comprehension is a loop that runs players times. 
# The loop generates 0 for each iteration, effectively creating a list of zeros with a length equal 
# to the value of players.
# For example, if players is 4, the resulting player_scores list will look like this: [0, 0, 0, 0]. 
# It's a common technique to initialize a list with a specific value repeated for each element.
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)