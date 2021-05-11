import click
import random
from words import word_list


def get_word():
    # get random word from list
    word = random.choice(word_list)
    return word.upper()


def play(word):
    # game will let you guess the entire word or a letter at a time
    # converts all word chars to underscores
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    # game loop active as long as the word is not guessed and there are more than 0 tries
    while not guessed and tries > 0:
        guess = input("Please guess a letter or a word: ").upper()
        # if the user typed one letter
        if len(guess) == 1 and guess.isalpha():
            # if they already guessed the letter
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            # if letter's not in the word
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            # if letter's in the word
            else:
                print("Good job,", guess, "is in the word")
                guessed_letters.append(guess)
                # converts word completion to list, so we can index into it
                word_as_list = list(word_completion)
                # enumerate on word so we can get both index i and letter at index for each iteration
                indices = [i for i, letter in enumerate(word) if letter == guess]
                # replaces each _ with the letter guessed
                for index in indices:
                    word_as_list[index] = guess
                # converts back to string
                word_completion = "".join(word_as_list)
                # if there are no underscores left, that means all letters were guessed
                if "_" not in word_completion:
                    guessed = True

        # same logic as above, but in case user tries to guess the entire word
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You've already guessed the word", guess)
            elif guess != word:
                print(guess, "is not in word")
                tries -= 1
            else:
                guessed = True
                word_completion = word

        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congratulations, you've guessed the word. You win!")
    else:
        print("You lose. The word was " + word + ". Maybe next time...")


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def cli():
    word = get_word()
    play(word)
    while input("Play again? (Y/N)").upper == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    cli()
