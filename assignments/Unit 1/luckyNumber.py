'''
Program: luckyNumber.py
Author: Mason Curtis
'''
import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()

# Main game loop - play multiple rounds
# To do: Use while True loop with break statement here
while True:
    # Generate random lucky number
    # To do: Use random.randint() to generate number between 1 and 50
    randNum = random.randint(1, 50)
    # Set maximum attempts
    # To do: Set max_attempts to 7
    max_attempts = 7
    # Initialize attempt counter
    # To do: Create attempts variable starting at 0
    attempts = 0
    print(f"\nRound {total_rounds + 1}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {max_attempts} attempts to guess it!")
    print()
   
    # Guessing loop - count-controlled while loop
    # To do: Use while loop that continues while attempts < max_attempts
    while attempts < max_attempts:
        # Get user's guess
        # To do: Get input and convert to integer
       guess = int(input("Enter a number between 1 and 50"))
        # Increment attempt counter
        # To do: Add 1 to attempts
       attempts += 1
        # Check if guess is correct
        # To do: Compare guess to lucky_number
       if guess == randNum:
          print("You win!")
          total_wins += 1
          total_rounds += 1
            # Player wins!
            # To do: Display success message
            # To do: Update statistics
            # To do: Break out of guessing loop
           
        # Provide hints
        # To do: Tell user if guess is too high or too low
       
    # If loop completes without break, player lost
    # To do: Handle case where player runs out of attempts
   
    # Display round statistics
    # To do: Show attempts used, win/loss for this round
   
    # Ask if player wants to play again
    # To do: Get input and check if user wants to continue
    # To do: Use break statement to exit main game loop if done
    if attempts > max_attempts:
       
# Display final statistics
# To do: Show total rounds, wins, and average guesses per round

#print("\nThanks for playing! Goodbye!")