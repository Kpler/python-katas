def compare_hands(hand1, hand2):
    """
    Compare two poker hands and determine the winner.

    Args:
        hand1 (list): The first poker hand.
        hand2 (list): The second poker hand.

    Returns:
        str: A message indicating which hand wins or if it's a tie.
    """
    # Placeholder for actual comparison logic
    # This should be replaced with the actual implementation that compares the hands
    if len(hand1) > len(hand2):
        return "Hand 1 wins"
    elif len(hand1) < len(hand2):
        return "Hand 2 wins"
    else:
        return "It's a tie"