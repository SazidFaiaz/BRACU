def minimax_with_mind_control(depth, is_maximizing, alpha, beta, maxV, minV, use_mind_control):
    if depth == 0:
        return utility(maxV, minV)

    if is_maximizing:
        max_eval = float('-inf')
        for move in range(2):  # Two possible moves
            if use_mind_control:
                eval = minimax_with_mind_control(depth - 1, False, alpha, beta, maxV, minV, False)
            else:
                eval = minimax_with_mind_control(depth - 1, False, alpha, beta, maxV, minV, use_mind_control)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for _ in range(2):  # Two possible moves
            eval = minimax_with_mind_control(depth - 1, True, alpha, beta, maxV, minV, use_mind_control)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval


def simulate_magic_game(starting_player, cost, light_strength, l_strength):
    if starting_player == 0:  # Light is Max
        maxV, minV = light_strength, l_strength
    else:
        maxV, minV = l_strength, light_strength

    without_magic = minimax_with_mind_control(5, True, float('-inf'), float('inf'), maxV, minV, False)
    with_magic = minimax_with_mind_control(5, True, float('-inf'), float('inf'), maxV, minV, True)
    with_magic_after_cost = with_magic - cost

    print(f"Minimax value without Mind Control: {without_magic:.2f}")
    print(f"Minimax value with Mind Control: {with_magic:.2f}")
    print(f"Minimax value with Mind Control after incurring the cost: {with_magic_after_cost:.2f}")

    if with_magic_after_cost > without_magic:
        print("Light should use Mind Control.")
    else:
        print("Light should NOT use Mind Control.")


def main_magic():
    starting_player = int(input("Enter who goes first (0 for Light, 1 for L): "))
    cost = float(input("Enter the cost of using Mind Control: "))
    light_strength = float(input("Enter base strength for Light: "))
    l_strength = float(input("Enter base strength for L: "))

    simulate_magic_game(starting_player, cost, light_strength, l_strength)


if __name__ == "__main__":
    main_magic()