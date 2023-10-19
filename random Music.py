import random

# List of music genres
music_genres = ["Rock", "Pop", "Classical", "Jazz"]

# Shuffle the list randomly
random.shuffle(music_genres)

# Select a random music genre from the list
selected_genre = random.choice(music_genres)

# Number of chances for the player to guess correctly
max_chances = 2
chances_left = max_chances

# Welcome message
print("Welcome to the Music Genre Guessing Game!")
print(f"I have selected a random music genre from this list (Rock, Pop, Classical, Jazz) Please Guest and type. You have {max_chances} chances to guess it.")

# Game loop
while chances_left > 0:
    # Ask the player to input their guess
    guess = input("Guess the music genre: ")

    # Check if the guess is correct
    if guess.lower() == selected_genre.lower():
        print("Congratulations! You guessed the music genre correctly!")
        break
    else:
        chances_left -= 1
        if chances_left > 0:
            print(f"Wrong guess. You have {chances_left} chances left.")
        else:
            print(f"Sorry, you've run out of chances. The correct genre was {selected_genre}. Game over!")

# End of the game
print("Thanks for playing the Music Genre Guessing Game!")  