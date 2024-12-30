import random

def flip():
    return random.random() < 0.70  # 51% chance to win

def play_game():
    bank = 0  # Initialize the banked points to 0
    points = 0  # Start with 1 point initially

    print(f"\n\n\n\n\n\n\n\n")

    while True:  # Main game loop
        # Add 0.1 points to the current points at the start of each turn
        points += 1
        
        print(f"\n\n--CoinFlip--")
        print(f"Points: {points}")  # Display current points
        print(f"Bank: {bank}\n")  # Display total banked points
        
        # Print the prompt with possible actions every turn
        action = input("Would you like to Flip, Bank, Withdraw, Wait, or Quit? ").lower()  # Get player action

        if action.startswith("flip"):
            modifier = action.split(" ")[1] if len(action.split(" ")) > 1 else None
            
            if modifier:
                if "%" in modifier:
                    percentage = int(modifier.strip("%"))
                    if percentage <= 0 or percentage > 100:
                        print("\nInvalid percentage. Please use a value between 1 and 100.")
                        continue
                    wager = points * (percentage / 100)
                else:
                    wager = int(modifier)
                    if wager <= 0 or wager > points:
                        print(f"\nInvalid amount. You can only flip between 1 and {points} points.")
                        continue
            else:
                wager = points  # If no modifier, flip all points
            
            wager = wager  # Ensure it's an integer
            
            if flip():  # Perform the coin flip
                points += wager  # Add the wagered amount to points
                print(f"\nYou won! Your points increased by {wager} to {points}.")
            else:
                points -= wager  # Subtract the wagered amount from points
                points = round(points)
                if points < 0:
                    points = 0  # Ensure points don't go negative
                print(f"\nYou lost the flip. Your points decreased to {points}.")
                
        elif action == "bank":
            if points <= 0:
                print("\nYou need more than 0 points to bank.")
                continue  # Return to the prompt without incrementing or counting as a turn
            try:
                amount = int(input("How many points do you want to bank? "))
                if amount <= 0:
                    print("\nYou must bank a positive amount.")
                    continue  # Return to the prompt without incrementing or counting as a turn
                if amount > points:
                    print(f"\nYou cannot bank more points than you have. You have {points} points.")
                    continue  # Return to the prompt without incrementing or counting as a turn
                bank += amount  # Add the specified amount to the bank
                points -= amount  # Subtract the banked amount from current points
                print(f"\nYou banked {amount} points. Total banked points: {bank}. Remaining points: {points}.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                continue  # Return to the prompt without incrementing or counting as a turn

        elif action == "withdraw":
            if bank == 0:
                print("\nYou have no points in the bank to withdraw.")
                continue  # Return to the prompt without incrementing or counting as a turn
            try:
                amount = int(input("\nHow many points do you want to withdraw? "))
                if amount <= 0:
                    print("\nYou must withdraw a positive amount.")
                    continue  # Return to the prompt without incrementing or counting as a turn
                if amount > bank:
                    print(f"\nYou cannot withdraw more than you have in the bank. You have {bank} points in the bank.")
                    continue  # Return to the prompt without incrementing or counting as a turn
                bank -= amount  # Subtract the specified amount from the bank
                points += amount  # Add the withdrawn amount to current points
                print(f"\nYou withdrew {amount} points. Total banked points: {bank}. Current points: {points}.")
            except ValueError:
                print("\nInvalid input. Please enter a number.")
                continue  # Return to the prompt without incrementing or counting as a turn

        elif action == "wait" or action == "":
            print("\nTurn skipped.")
            
        elif action == "quit":
            print(f"\nThanks for playing! You ended with {bank + points} total points.\n")  # End the game and show total banked points
            break  # Exit the game loop
            
        else:
            print("\nInvalid choice. Please choose 'flip', 'bank', 'wait', or 'quit'.")
            continue  # Return to the prompt without incrementing or counting as a turn

if __name__ == "__main__":
    play_game()  # Run the game when the script is executed
