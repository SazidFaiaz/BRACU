#22101309_MD. SAZID FAIAZ_sec4

import random
import math

def strength(x):
    return math.log2(x+1)+x/10

def utility(maxval, minval):
    i = random.randint(0, 1)
    return strength(maxval) - strength(minval) + ((-1) ** i) * random.randint(1,10)/10

def pruning(depth, maxplayer, alpha, beta, maxval, minval):
    if depth == 0:
        return utility(maxval, minval)
    if maxplayer:
        maxlevel = float('-inf')
        for _ in range(2):
            val = pruning(depth - 1, False, alpha, beta, maxval, minval)
            maxlevel = max(maxlevel, val)
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return maxlevel

    else:
        minlevel = float('inf')
        for _ in range(2):
            val = pruning(depth - 1, True, alpha, beta, maxval, minval)
            minlevel = min(minlevel, val)
            beta = min(beta, val)
            if beta <= alpha:
                break
        return minlevel

def start_game(starting, player1, player2):
    results = []
    rounds = 4
    for game in range(rounds):
        if (starting + game) % 2 == 0:
            maxval, minval = player1, player2
            winner = "Magnus Carlsen"
        else:
            maxval, minval = player1, player2
            winner = "Fabiano Caruana"

        win_value = pruning(5, True, float('-inf'), float('inf'), maxval, minval)
        if win_value > 0:
            results.append((winner, win_value))
        elif win_value < 0:
            results.append((f"{'Fabiano Caruana' if winner == 'Magnus Carlsen' else 'Magnus Carlsen'}", win_value))
        else:
            results.append(("Draw", win_value))

    return results

def main():
    starting = int(input("Enter starting player for game 1 (0 for Carlsen, 1 for Caruana): "))
    player1 = float(input("Enter base strength for Carlsen: "))
    player2 = float(input("Enter base strength for Caruana: "))

    results = start_game(starting, player1, player2)

    player1_wins = sum(1 for result in results if result[0] == "Magnus Carlsen")
    player2_wins = sum(1 for result in results if result[0] == "Fabiano Caruana")
    draws = sum(1 for result in results if result[0] == "Draw")

    print("\nGame Results:")
    for i, (winner, utility_value) in enumerate(results, 1):
        print(f"Game {i} Winner: {winner} (Utility value: {utility_value:.2f})")

    print("\nOverall Results:")
    print(f"Magnus Carlsen Wins: {player1_wins}")
    print(f"Fabiano Caruana Wins: {player2_wins}")
    print(f"Draws: {draws}")

    if player1_wins > player2_wins:
        print("Overall Winner: Magnus Carlsen")
    elif player2_wins > player1_wins:
        print("Overall Winner: Fabiano Caruana")
    else:
        print("Overall Winner: Draw")


if __name__ == "__main__":
    main()

