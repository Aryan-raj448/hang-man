import random


# List of words related to Computer Science
word_list = [
    "algorithm", "function", "variable", "compile", "iterate", 
    "recursion", "binary", "array", "syntax", "pointer"
]

def display_hangman(incorrect_guesses):
    """Displays the HANGMAN header and the pointer."""
    print("HANGMAN")
    print(" " * incorrect_guesses + "^")  # move the pointer based on wrong guesses

def display_word_progress(word, guessed_letters):
    """Displays the current state of the word with guessed letters."""
    display = [letter if letter in guessed_letters else "_" for letter in word]
    print(" ".join(display))

def get_valid_guess():
    """Ensures that the user inputs a valid, single alphabetic character."""
    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid input. Please enter a single alphabetic character.")

def play_game():
    """Main function to play a Hangman game."""
    word = random.choice(word_list)  # Randomly select a word
    guessed_letters = set()  # Set of correctly guessed letters
    incorrect_guesses = 0  # Counter for incorrect guesses
    max_incorrect_guesses = 6  # Max incorrect guesses before losing

    print("Welcome to Hangman!")
    while incorrect_guesses < max_incorrect_guesses:
        # Display the HANGMAN and the current state of the word
        display_hangman(incorrect_guesses)
        display_word_progress(word, guessed_letters)
        
        # Check if the word has been fully guessed
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: '{word}'")
            print("Phew... you are saved.")
            return
        
        # Ask for a guess
        guess = get_valid_guess()
        
        # If the guess has been made before, notify the player
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Wrong guess!")
    
    # If the max incorrect guesses is reached
    display_hangman(incorrect_guesses)
    print("You are hanged!")
    print("-----|")
    print("  |  |")
    print("  O  |")
    print(" /|\\ |")
    print(" / \\ |")
    print("     |")
    print("_____|")
    print(f"The word was: {word}")

def main():
    """Controls the flow of the Hangman game and prompts the user to replay."""
    while True:
        play_game()
        
        # Ask if the player wants to play again
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()

