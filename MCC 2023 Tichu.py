def longest_run(N, K, cards):
    # Sort the list of integers in ascending order
    cards.sort()

    max_run_length = 0
    current_run_length = 1

    for i in range(1, N-K):
        current_integer = cards[i]
        previous_integer = cards[i-1]

        if current_integer == previous_integer + 1:
            current_run_length += 1
        else:
            wild_cards_needed = current_integer - previous_integer - 1

            if wild_cards_needed <= K:
                current_run_length += wild_cards_needed
            else:
                current_run_length += K

        if current_run_length > max_run_length:
            max_run_length = current_run_length

    return max_run_length

# Read the input
N, K = map(int, input().split())
cards = list(map(int, input().split()))

# Call the function and print the result
result = longest_run(N, K, cards)
print(result)
